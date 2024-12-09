# companies/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request):
        """
        List all companies with basic information
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific company by ID
        """
        try:
            company = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(company)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response({
                'error': 'Company not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """
        Create a new company
        """
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Additional validation for company name
            name = serializer.validated_data.get('name')
            if Company.objects.filter(name__iexact=name).exists():
                return Response({
                    'error': 'A company with this name already exists'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Save the company
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Update an existing company
        """
        try:
            company = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(company, data=request.data, partial=True)
            
            if serializer.is_valid():
                # Additional validation for company name
                name = serializer.validated_data.get('name')
                if name:
                    existing_company = Company.objects.filter(name__iexact=name).exclude(pk=pk)
                    if existing_company.exists():
                        return Response({
                            'error': 'A company with this name already exists'
                        }, status=status.HTTP_400_BAD_REQUEST)
                
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Company.DoesNotExist:
            return Response({
                'error': 'Company not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """
        Delete a company
        """
        try:
            company = self.get_queryset().get(pk=pk)
            
            # Check if company has departments or employees before deletion
            if company.number_of_departments > 0 or company.number_of_employees > 0:
                return Response({
                    'error': 'Cannot delete company with existing departments or employees'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Company.DoesNotExist:
            return Response({
                'error': 'Company not found'
            }, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['GET'])
    def stats(self, request, pk=None):
        """
        Get detailed statistics for a specific company
        """
        try:
            company = self.get_queryset().get(pk=pk)
            return Response({
                'name': company.name,
                'departments_count': company.number_of_departments,
                'employees_count': company.number_of_employees
            })
        except Company.DoesNotExist:
            return Response({
                'error': 'Company not found'
            }, status=status.HTTP_404_NOT_FOUND)

