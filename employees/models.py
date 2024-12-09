from django.db import models
from companies.models import Company
from departments.models import Department
from datetime import date

class Employee(models.Model):
    STATUS_CHOICES = [
        ('Onboarding', 'Onboarding'),
        ('Hired', 'Hired'),
        ('Terminated', 'Terminated'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        related_name='employees',
        limit_choices_to={'company': models.F('company')}  # Limit departments to the selected company
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Onboarding')
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    designation = models.CharField(max_length=255)
    hired_on = models.DateField(null=True, blank=True)

    @property
    def days_employed(self):
        if self.hired_on:
            return (date.today() - self.hired_on).days
        return None

    def __str__(self):
        return f"{self.name} ({self.designation})"
