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
	alquiler = models.ManyToManyField(Cliente)