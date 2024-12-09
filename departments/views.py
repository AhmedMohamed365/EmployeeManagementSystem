# companies/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request):
        """
        List all departments with basic information
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific deprtment by ID
        """
        try:
            department = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(department)
            return Response(serializer.data)
        except department.DoesNotExist:
            return Response({
                'error': 'department not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """
        Create a new department
        """
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Additional validation for department name
            name = serializer.validated_data.get('name')
            if Department.objects.filter(name__iexact=name).exists():
                return Response({
                    'error': 'A department with this name already exists'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Save the department
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Update an existing department
        """
        try:
            department = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(department, data=request.data, partial=True)
            
            if serializer.is_valid():
                # Additional validation for department name
                name = serializer.validated_data.get('name')
                if name:
                    existing_department = department.objects.filter(name__iexact=name).exclude(pk=pk)
                    if existing_department.exists():
                        return Response({
                            'error': 'A department with this name already exists'
                        }, status=status.HTTP_400_BAD_REQUEST)
                
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except department.DoesNotExist:
            return Response({
                'error': 'department not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """
        Delete a department
        """
        try:
            department = self.get_queryset().get(pk=pk)
            
            # Check if department has departments or employees before deletion
            if department.number_of_departments > 0 or department.number_of_employees > 0:
                return Response({
                    'error': 'Cannot delete department with existing departments or employees'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            department.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except department.DoesNotExist:
            return Response({
                'error': 'department not found'
            }, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['GET'])
    def stats(self, request, pk=None):
        """
        Get detailed statistics for a specific department
        """
        try:
            department = self.get_queryset().get(pk=pk)
            return Response({
                'name': department.name,
                'departments_count': department.number_of_departments,
                'employees_count': department.number_of_employees
            })
        except department.DoesNotExist:
            return Response({
                'error': 'department not found'
            }, status=status.HTTP_404_NOT_FOUND)

