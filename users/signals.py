from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import User

@receiver(post_migrate)
def setup_default_groups(sender, **kwargs):
    admin_group, _ = Group.objects.get_or_create(name='Admin')
    manager_group, _ = Group.objects.get_or_create(name='Manager')
    employee_group, _ = Group.objects.get_or_create(name='Employee')

    # Assign Permissions (example)
    user_content_type = ContentType.objects.get_for_model(User)
    add_permission = Permission.objects.get(codename='add_user', content_type=user_content_type)

    admin_group.permissions.add(add_permission)
    # Add other permissions as needed
