# user/permissions.py
from rest_framework.permissions import BasePermission

class CanEditEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Manager' or request.user.role == 'Admin'

class CanViewEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['Admin', 'Manager', 'Employee']
