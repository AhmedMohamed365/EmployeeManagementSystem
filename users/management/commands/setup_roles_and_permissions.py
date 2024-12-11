from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from employees.models import Employee, Department, Company
class Command(BaseCommand):
    help = 'Sets up roles (Admin, Manager, Employee) and assigns permissions'

    def handle(self, *args, **kwargs):
        # Step 1: Create permissions
        #create_permissions()

        # Step 2: Create groups (roles)
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        manager_group, _ = Group.objects.get_or_create(name="Manager")
        employee_group, _ = Group.objects.get_or_create(name="Employee")

        # Step 3: Get ContentTypes for models
        employee_content_type = ContentType.objects.get_for_model(Employee)
        department_content_type = ContentType.objects.get_for_model(Department)
        company_content_type = ContentType.objects.get_for_model(Company)

        # Step 4: Assign permissions to groups

        # Admin permissions (Full access)
        admin_permissions = Permission.objects.filter(content_type__in=[employee_content_type, department_content_type, company_content_type])
        admin_group.permissions.set(admin_permissions)

        # Manager permissions (Limited access)
        manager_permissions = [
            # Employee model: view, add, change, and change status (not delete)
            'view_employee', 'add_employee', 'change_employee', 'change_employee_status',
            # Department model: view and change
            'view_department', 'change_department',
            # Company model: view
            'view_company'
        ]
        manager_permissions = Permission.objects.filter(
            codename__in=manager_permissions,
            content_type__in=[employee_content_type, department_content_type, company_content_type]
        )
        manager_group.permissions.set(manager_permissions)

        # Employee permissions (Only view own data)
        employee_permissions = [
            # Employee model: view only their own details
            'view_employee',
            # Company model: view basic company details
            'view_company',
            # Department model: view their own department details
            'view_department',
        ]
        employee_permissions = Permission.objects.filter(
            codename__in=employee_permissions,
            content_type__in=[employee_content_type, department_content_type, company_content_type]
        )
        employee_group.permissions.set(employee_permissions)

        # Output success message
        self.stdout.write(self.style.SUCCESS('Roles and permissions have been set up successfully!'))
