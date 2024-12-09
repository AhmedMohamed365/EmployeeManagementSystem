
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from departments.models import Department
from companies.models import Company
from employees.models import Employee

# Optional: Use signals as a backup mechanism
@receiver(post_save, sender=Employee)
def update_employee_counts_on_save(sender, instance, created, **kwargs):
    """
    Signal to update counts when an employee is saved
    """
    if created:
        instance.Department.update_department_employee_count()
        instance.Department.update_company_employee_count()

@receiver(post_delete, sender=Employee)
def update_employee_counts_on_delete(sender, instance, **kwargs):
    """
    Signal to update counts when an employee is deleted
    """
    instance.Department.update_department_employee_count()
    instance.Department.update_company_employee_count()