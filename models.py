from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.DateField(max_length=30)
    fecha = models.DateTimeField(max_length=30)
