from rest_framework import exceptions
from rest_framework import permissions


class CustomDjangoModelPermissions(permissions.DjangoModelPermissions):
    view_perm = '%(app_label)s.view_%(model_name)s'
    perms_map = {
        'GET': [view_perm],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def __init__(self, custom_permission=None):
        self.custom_permission = custom_permission

    def __call__(self):
        return self
    
    def get_required_permissions(self, method, model_cls):
        """
        Given a model and an HTTP method, return the list of permission
        codes that the user is required to have.
        """
        if self.custom_permission:
            return [f'{model_cls._meta.app_label}.{self.custom_permission}']

        kwargs = {
            'app_label': model_cls._meta.app_label,
            'model_name': model_cls._meta.model_name
        }

        if method not in self.perms_map:
            raise exceptions.MethodNotAllowed(method)

        return [perm % kwargs for perm in self.perms_map[method]]
