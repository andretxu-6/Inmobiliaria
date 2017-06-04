from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from apps.inmuebles.models import Inmueble
from apps.inmuebles.forms import InmuebleForm
# Create your views here.

class Inmuebles(ListView):
	model = Inmueble
	template_name = "inmuebles/index.html"


class inmueble_view(CreateView):
	model = Inmueble
	form_class = InmuebleForm
	template_name = 'inmuebles/inmuebles_form.html'
	success_url = reverse_lazy("inmuebles")

class inmueble_edit(UpdateView):
	model = Inmueble
	form_class = InmuebleForm
	template_name = 'inmuebles/inmuebles_form.html'
	success_url = reverse_lazy("inmuebles")

class inmueble_delete(DeleteView):
	model = Inmueble
	template_name = 'inmuebles/inmuebles_delete.html'
	success_url = reverse_lazy("inmuebles")

#def inmuebles(request):
	#inmueble_tot = Inmueble.objects.all().order_by('id')
	#enviar = {'inmuebles': inmueble_tot}
	#return render(request, 'inmuebles/index.html',enviar)


#def inmueble_view(request):
#	if request.method == 'POST':
#		form = InmuebleForm(request.POST)
#		if form.is_valid():
#			form.save()
#		return redirect('inmuebles')
#	else:
#		form = InmuebleForm()

#	return render(request, 'inmuebles/inmuebles_form.html', {'form': form})


#def inmueble_edit(request, id_inmueble):
#	inmueb = Inmueble.objects.get(id=id_inmueble)
#	if request.method == 'GET':
#		form = InmuebleForm(instance=inmueb)
#	else:
#		form = InmuebleForm(request.POST, instance=inmueb)
#		if form.is_valid():
#			form.save()
#		return redirect('inmuebles')
#	return render(request, "inmuebles/inmuebles_form.html", {'form':form})
