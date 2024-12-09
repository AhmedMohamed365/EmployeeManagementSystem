from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'company', 'company_name', 'number_of_employees']
        read_only_fields = ['number_of_employees']

    def get_company_name(self, obj):
        return obj.company.name  # Access the related company's name
