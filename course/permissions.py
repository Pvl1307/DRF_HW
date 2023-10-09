from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'update']:
            return self.has_permission(request, view)
        return False


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve', 'update']:
            return obj.owner == request.user
        return False
