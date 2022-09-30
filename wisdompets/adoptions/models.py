from asyncio.windows_events import NULL
from random import choices
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Pet(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')]
    name = models.CharField(_MAX_LENGTH = 100)
    submitter = models.CharField(_MAX_LENGTH = 100)
    species = models.CharField(_MAX_LENGTH = 30)
    breed = models.CharField(_MAX_LENGTH = 30, blank_re = True)
    description = models.TextField()
    sex = models.CharField(_MAX_LENGTH = 1 , choices = SEX_CHOICES , blank_re= True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(NULL = True)
    vaccinations = models.ManyToManyField('Vaccine', blank_re=True)


class Vaccine(models.Model):
    name = models.CharField(_MAX_LENGTH = 50)

