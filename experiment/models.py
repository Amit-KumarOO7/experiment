from enum import unique
from django.db import models
from matplotlib import widgets
from sympy import Max

# Create your models here.

class Rootcaim(models.Model):
    name = models.CharField(max_length=64)
    common_name = models.CharField(max_length=264,blank=False, help_text='enter url')
    validity_time = models.IntegerField(help_text='Validity time in years')
    country_code = models.CharField(max_length=2, blank=True)
    state = models.CharField(max_length=64, blank=True)
    org_name = models.CharField(max_length=64, blank=True)
    org_unit = models.CharField(max_length=64, blank=True)
    certificate = models.TextField(unique=True)

    def __str__(self) -> str:
        return self.name