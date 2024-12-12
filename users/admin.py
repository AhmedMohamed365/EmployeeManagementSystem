# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

class CustomUserAdmin(UserAdmin):
    # Customize the list display in the admin panel
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'date_joined')
    
    # Customize filtering options
    list_filter = ('is_active', 'is_staff', 'role')
    
    # Customize search fields
    search_fields = ('username', 'email')
    
    # Customize the fieldsets for editing a user
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal Info'), {'fields': ('role',)}),
        (_('Permissions'), {
            'fields': (
                'is_active', 
                'is_staff', 
                'is_superuser', 
                'groups', 
                'user_permissions'
            )
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Customize the fieldsets for creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 
                'email', 
                'password1', 
                'password2', 
                'role', 
                'is_active', 
                'is_staff'
            )
        }),
    )
    
    # Specify the ordering in the admin panel
    ordering = ('-date_joined',)

# Register the model with the custom admin configuration
admin.site.register(User, CustomUserAdmin)