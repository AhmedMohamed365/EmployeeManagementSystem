# user/management/commands/setup_roles_and_permissions.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Sets up roles (Admin, Manager, Employee) and assigns permissions'

    def handle(self, *args, **kwargs):
        # Create groups (roles)
        admin_group, created = Group.objects.get_or_create(name="Admin")
        manager_group, created = Group.objects.get_or_create(name="Manager")
        employee_group, created = Group.objects.get_or_create(name="Employee")

        # Define permissions (permissions can be customized)
        permissions = [
            ("view_employee", "Can view employee"),
            ("add_employee", "Can add employee"),
            ("change_employee", "Can change employee"),
            ("delete_employee", "Can delete employee"),
        ]

        # Create and assign permissions
        for perm_codename, perm_name in permissions:
            permission, created = Permission.objects.get_or_create(
                codename=perm_codename, 
                name=perm_name,
                content_type=ContentType.objects.get_for_model(Group)  # This makes the permission related to a group
            )
            # Assign permissions to groups based on the role
            if perm_codename in ["view_employee", "change_employee"]:
                admin_group.permissions.add(permission)
                manager_group.permissions.add(permission)
            if perm_codename == "view_employee":
                employee_group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Roles and permissions have been set up successfully!'))
