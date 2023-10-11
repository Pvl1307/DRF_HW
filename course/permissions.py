from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moders').exists() and request.method in ['POST', 'DELETE']:
            return False
        if request.user.groups.filter(name='moders').exists() and request.method in ['GET', 'PUT', 'PATCH']:
            return True
        return True


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return request.method in ['GET', 'PUT', 'PATCH', 'DELETE']
        return False

