from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Department


@receiver(post_save, sender=Department)
def update_company_department_count_on_save(sender, instance, created, **kwargs):
    """
    Signal to update the number of departments in a company when a new department is created.
    """
    if created:  # Only update count when a department is newly created
        company = instance.company  # Use the correct field name
        company.number_of_departments += 1
        company.save()  # Save the updated company instance


@receiver(post_delete, sender=Department)
def update_company_department_count_on_delete(sender, instance, **kwargs):
    """
    Signal to update the number of departments in a company when a department is deleted.
    """
    company = instance.company  # Use the correct field name
    company.number_of_departments -= 1
    company.save()  # Save the updated company instance

