from rest_framework import serializers
from .models import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, data):
        """
        Ensure the selected department belongs to the specified company.
        """
        company = data.get('company')
        department = data.get('department')

        if department and department.company != company:
            raise serializers.ValidationError("The selected department does not belong to the specified company.")
        return data
