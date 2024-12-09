from django.db import models
from companies.models import Company

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    number_of_employees = models.PositiveIntegerField(default=0)

    def update_employee_count(self):
        """
        Update the number of employees in the department
        """
        # Use annotation to get the exact count
        count = self.employee_set.count()
        
        # Only save if count has changed to minimize database writes
        if self.number_of_employees != count:
            self.number_of_employees = count
            self.save(update_fields=['number_of_employees'])

            
    def __str__(self):
        return f"{self.name} ({self.company.name})"
    

