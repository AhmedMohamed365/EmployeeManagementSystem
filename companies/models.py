from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    number_of_departments = models.PositiveIntegerField(default=0)
    number_of_employees = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
