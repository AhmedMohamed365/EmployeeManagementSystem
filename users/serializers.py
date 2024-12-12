# serializers.py
# serializers.py
from djoser.serializers import UserCreateSerializer ,UserSerializer
from rest_framework import serializers
from .models import User

class CustomUserCreateSerializer(UserCreateSerializer):
    role = serializers.ChoiceField(
        choices=User.ROLE_CHOICES,
        required=True,  # Make role a required field
        help_text="Select a user role during registration"
    )

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'role')

    
    

    def create(self, validated_data):
        # Create user using the custom create_user method
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data.get('username', validated_data['email'].split('@')[0]),
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'role')