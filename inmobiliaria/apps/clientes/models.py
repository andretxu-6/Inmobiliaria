from django.db import models

# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length=20)
	apellidos = models.CharField(max_length=40)
	fecha_nacimiento = models.DateField()
	telefono = models.CharField(max_length=15)
	email = models.EmailField(max_length=20)