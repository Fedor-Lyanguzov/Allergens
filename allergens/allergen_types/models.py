from django.db import models

class AllergenClass(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class AllergenType(models.Model):
    klass = models.ForeignKey(AllergenClass)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

