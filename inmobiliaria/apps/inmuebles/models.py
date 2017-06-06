from django.db import models
from apps.ciudades.models import Ciudad
from apps.propietarios.models import Propietario
from apps.clientes.models import Cliente

# Create your models here.
class Inmueble(models.Model):
	direccion = models.CharField(max_length=150)
	metros = models.IntegerField()
	precio = models.IntegerField()
	habitaciones = models.IntegerField()
	descripccion = models.CharField(max_length=300)
	opcion = models.CharField(max_length=2)
	disponibilidad = models.BooleanField()
	ciudad = models.ForeignKey(Ciudad, null=True, blank=True, on_delete=models.CASCADE)
	propietario = models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.CASCADE)
	alqui = models.ManyToManyField(Cliente, through='alquiler', blank=True)

	def __str__(self):
		return '{}'.format(self.direccion)

class alquiler(models.Model):
	inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	fecha_entrada = models.DateField()
	fecha_salida = models.DateField()