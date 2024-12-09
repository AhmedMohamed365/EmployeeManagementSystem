from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class EmployeeRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        data['role'] = 'Employee'  # Force the role to be Employee
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.permissions import BasePermission, IsAuthenticated


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Admin'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Manager'

class CreateManagerView(APIView):
    permission_classes = [IsAdmin]  # Only Admins can create managers

    def post(self, request):
        # Logic for creating a manager
        pass

class EmployeeView(APIView):
    permission_classes = [IsAuthenticated]  # All authenticated users can access

    def get(self, request):
        # Logic for employees to view data
        pass
