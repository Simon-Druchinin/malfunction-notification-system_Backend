def django_permission_to_casl_ability(permissions: list[dict]):
    casl_ability = [{'action': 'manage', 'subject': 'default'}] # Initial ability for authenticated users

    for permission in permissions:
        action, subject = permission['codename'].split('_')
        casl_ability.append({'action': action, 'subject': subject})

    return casl_ability
