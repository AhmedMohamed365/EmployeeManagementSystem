from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'number_of_departments', 'number_of_employees']
        read_only_fields = ['number_of_departments', 'number_of_employees']