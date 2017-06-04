from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from apps.propietarios.models import Propietario
from apps.propietarios.forms import PropietarioForm
# Create your views here.

class Propietarios(ListView):
	model = Propietario
	template_name = "propietarios/index.html"

class propietarios_view(CreateView):
	model = Propietario
	form_class = PropietarioForm
	template_name = 'propietarios/propietarios_form.html'
	success_url = reverse_lazy("listado_propietarios")

class propietarios_edit(UpdateView):
	model = Propietario
	form_class = PropietarioForm
	template_name = 'propietarios/propietarios_form.html'
	success_url = reverse_lazy("listado_propietarios")

class propietarios_delete(DeleteView):
	model = Propietario
	template_name = 'propietarios/propietarios_delete.html'
	success_url = reverse_lazy("listado_propietarios")