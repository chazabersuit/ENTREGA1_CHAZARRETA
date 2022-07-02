from msilib.schema import Class
from django.db import models

# Create your models here.
class Videos(models.Model):
    interprete=models.CharField(max_length=50)
    album=models.CharField(max_length=50)
    año=models.DateField()