from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from apps.usuarios.forms import RegistroForm
# Create your views here.

#los crea en la tabla auth_users
class RegistroUsuario(CreateView):
	model = User
	template_name = "usuarios/registro.html"
	form_class = RegistroForm
	success_url = reverse_lazy('inmuebles');