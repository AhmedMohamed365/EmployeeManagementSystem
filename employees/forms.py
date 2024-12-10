# from django import forms
# from .models import Employee,Department

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance and self.instance.company:
#             self.fields['department'].queryset = Department.objects.filter(company=self.instance.company)
