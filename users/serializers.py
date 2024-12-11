# serializers.py
from djoser.serializers import UserCreateSerializer , UserSerializer
from .models import User

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email', 'password', 'role')  # Include 'role'

    def create(self, validated_data):
        # Ensure role is provided, if not default to 'viewer'
        role = validated_data.get('role', 'employee')
        print(f'chosen role is {role}')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=role
        )
        return User

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'username', 'name','email', 'role')

