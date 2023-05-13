from django.contrib.auth.models import Permission

from users.models import User


def django_permission_to_casl_ability(permissions: list[dict], user: User=None):
    if user and user.is_staff and user.is_superuser:
        return [{'action': 'manage', 'subject': 'all'}]
    
    casl_ability = [{'action': 'manage', 'subject': 'default'}] # Initial ability for authenticated users

    for permission in permissions:
        action, subject = permission['codename'].split('_')
        casl_ability.append({'action': action, 'subject': subject})

    return casl_ability

def get_user_permissions(user: User):
    if user.is_superuser:
        return Permission.objects.all()
    return user.user_permissions.all() | Permission.objects.filter(group__user=user)

