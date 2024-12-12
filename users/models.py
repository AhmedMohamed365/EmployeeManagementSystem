from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role='viewer', **extra_fields):
        """
        Create and return a regular user with the specified role.
        """
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        
        # Normalize the email address
        email = self.normalize_email(email)
        
        # Create the user
        user = self.model(
            username=username, 
            email=email, 
            role=role,
            **extra_fields
        )
        
        # Set the password
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser.
        """
        # Ensure default values for superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'admin')

        # Validate superuser specific fields
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(
            username=username, 
            email=email, 
            password=password, 
            **extra_fields
        )

class User(AbstractBaseUser, PermissionsMixin):
    # Role choices
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('manager', 'Manager'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    ]

    # Basic user information
    username = models.CharField(
        max_length=50, 
        unique=True, 
        help_text="Enter a unique username"
    )
    email = models.EmailField(
        unique=True, 
        help_text="Enter a valid email address"
    )
    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='viewer',
        help_text="Select user role"
    )

    # Additional user management fields
    is_active = models.BooleanField(
        default=True, 
        help_text="Designates whether this user account should be treated as active"
    )
    is_staff = models.BooleanField(
        default=False, 
        help_text="Designates whether the user can access the admin site"
    )

    # Timestamp fields
    date_joined = models.DateTimeField(
        default=timezone.now, 
        help_text="Date and time when the user account was created"
    )
    last_login = models.DateTimeField(
        null=True, 
        blank=True, 
        help_text="Date and time of the user's last login"
    )

    # Define the fields that will be used for authentication
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'role']

    # Use the custom user manager
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
        permissions = [
            ("view_user_details", "Can view user details"),
            ("edit_user_role", "Can edit user role"),
        ]