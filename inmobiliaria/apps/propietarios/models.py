from django.db import models

# Create your models here.
class Propietario(models.Model):
	nombre = models.CharField(max_length=20)
	apellidos = models.CharField(max_length=40)
	fecha_nacimiento = models.DateField()
	direccion = models.CharField(max_length=150)
	telefono = models.CharField(max_length=15)
	email = models.EmailField()

	def __str__(self):
		return '{}'.format(self.nombre)