# from django.contrib import admin

# # Register your models here.
# from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
# from django.contrib import admin
# from .models import User

# class UserAdmin(DefaultUserAdmin):
#     def save_model(self, request, obj, form, change):
#         # Restrict who can create certain roles
#         if not request.user.is_superuser and obj.role in ['Admin', 'Manager']:
#             raise PermissionDenied("You don't have permission to create this role.")
#         super().save_model(request, obj, form, change)

# admin.site.register(User, UserAdmin)
