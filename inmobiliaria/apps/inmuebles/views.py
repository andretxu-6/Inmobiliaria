from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.inmuebles.models import Inmueble
from apps.inmuebles.forms import InmuebleForm
# Create your views here.
def inmuebles(request):
	#return HttpResponse("holadola caracola")
	#AQUI PODRIA HACER 2 SELECT, LAS CASAS DISPONIBLES Y LAS NO DISPONIBLES Y MANDAR LAS DOS, CON ESO CREAR LA TABLA EN EL TEMPLATE
	inmueble_tot = Inmueble.objects.all().order_by('id')
	enviar = {'inmuebles': inmueble_tot}
	return render(request, 'inmuebles/index.html',enviar)

def inmueble_view(request):
	if request.method == 'POST':
		form = InmuebleForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('inmuebles')
	else:
		form = InmuebleForm()

	return render(request, 'inmuebles/inmuebles_form.html', {'form': form})

def inmueble_edit(request, id_inmueble):
	inmueb = Inmueble.objects.get(id=id_inmueble)
	if request.method == 'GET':
		form = InmuebleForm(instance=inmueb)
	else:
		form = InmuebleForm(request.POST, instance=inmueb)
		if form.is_valid():
			form.save()
		return redirect('inmuebles')
	return render(request, "inmuebles/inmuebles_form.html", {'form':form})
