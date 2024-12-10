# companies/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request):
        """
        List all Employees with basic information
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific employee by ID
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
        Create a new Employee
        """
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Additional validation for Employee name
            name = serializer.validated_data.get('name')
            if Employee.objects.filter(name__iexact=name).exists():
                return Response({
                    'error': 'A Employee with this name already exists'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Save the Employee
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Update an existing Employee
        """
        try:
            employee = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(employee, data=request.data, partial=True)
            
            if serializer.is_valid():
                # Additional validation for Employee name
                email = serializer.validated_data.get('email')
                if email:
                    existing_Employee = Employee.objects.filter(email__iexact=email).exclude(pk=pk)
                    if existing_Employee.exists():
                        return Response({
                            'error': 'An  Employee with this email already exists'
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
        Delete a Employee
        """
        try:
            employee = self.get_queryset().get(pk=pk)
            
            
            
            
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Employee.DoesNotExist:
            return Response({
                'error': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['GET'])
    def stats(self, request, pk=None):
        """
        Get detailed statistics for a specific Employee
        """
        try:
            Employee = self.get_queryset().get(pk=pk)
            return Response({
                'name': Employee.name,
                'Employees_count': Employee.number_of_Employees,
                'employees_count': Employee.number_of_employees
            })
        except Employee.DoesNotExist:
            return Response({
                'error': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)

