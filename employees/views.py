from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

class IsAdminOrManager(permissions.BasePermission):
    """
    Custom permission to only allow Admin and Manager users to edit or delete employees.
    """
    def has_permission(self, request, view):
        # Only Admin and Manager can update or delete
        if view.action in ['update', 'destroy']:
            return request.user and request.user.role in ['Admin', 'Manager']
        return True  # Allow all authenticated users to list employees

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]  # Default to allowing authenticated users

    def list(self, request):
        """
        List all Employees with basic information. Accessible by all authenticated users.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific employee by ID.
        """
        try:
            employee = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response({
                'error': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """
        Create a new Employee. Only Admin and Manager roles are allowed.
        """
        if request.user.role not in ['admin', 'manager']:
            return Response({
                'error': 'You do not have permission to create employees'
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Additional validation for Employee name
            name = serializer.validated_data.get('name')
            if Employee.objects.filter(name__iexact=name).exists():
                return Response({
                    'error': 'An Employee with this name already exists'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Save the Employee
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Update an existing Employee. Only Admin and Manager roles are allowed.
        """
        if request.user.role not in ['admin', 'manager']:
            return Response({
                'error': 'You do not have permission to update employees'
            }, status=status.HTTP_403_FORBIDDEN)

        try:
            employee = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(employee, data=request.data, partial=True)
            
            if serializer.is_valid():
                # Additional validation for Employee email (optional)
                email = serializer.validated_data.get('email')
                if email:
                    existing_employee = Employee.objects.filter(email__iexact=email).exclude(pk=pk)
                    if existing_employee.exists():
                        return Response({
                            'error': 'An Employee with this email already exists'
                        }, status=status.HTTP_400_BAD_REQUEST)
                
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Employee.DoesNotExist:
            return Response({
                'error': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """
        Delete an Employee. Only Admin and Manager roles are allowed.
        """
        if request.user.role not in ['admin', 'manager']:
            return Response({
                'error': 'You do not have permission to delete employees'
            }, status=status.HTTP_403_FORBIDDEN)

        try:
            employee = self.get_queryset().get(pk=pk)
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Employee.DoesNotExist:
            return Response({
                'error': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)
