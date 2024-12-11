
from rest_framework.permissions import BasePermission 

class IsSuperUserOrAdmin(BasePermission):
    """
    Custom permission to only allow superusers to create users.
    """
    def has_permission(self, request, view):
        # Allow access only if the user is authenticated and is a superuser
        
        return request.user and  request.user.is_superuser


class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['Admin', 'Manager']).exists()

