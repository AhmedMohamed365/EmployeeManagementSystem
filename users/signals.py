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



# @receiver(post_save, sender=Employee)
# def create_user_for_employee(sender, instance, created, **kwargs):
#     if created:  # Ensure the signal only acts when a new instance is created
#         # Generate a random password
#         password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        
#         # Create the user
#         user = User.objects.create_user(
#             username=instance.email,  # Use email as the username
#             email=instance.email,
#             password=password
#         )
        
#         # Map role
#         user.is_staff = instance.role in ['Admin', 'Manager']  # Make Admin/Manager staff
#         user.save()

#         # Optional: Log or send email with the credentials
#         print(f"User created for {instance.name}. Password: {password}")
