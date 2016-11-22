from django.db import models

from allergen_types.models import AllergenType

class Patient(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    registration_date = models.DateField()
    years = models.IntegerField(null=True)
    months = models.IntegerField(null=True)
    attending_doctor = models.CharField(max_length=200)
    analyzes = models.ManyToManyField(AllergenType)
    
    def __str__(self):
        return ' '.join((self.last_name, self.first_name, self.middle_name))