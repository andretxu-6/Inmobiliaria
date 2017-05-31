from django.contrib import admin
from .models import Inmueble, alquiler

# Register your models here.
admin.site.register(Inmueble)
admin.site.register(alquiler)