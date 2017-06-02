from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.inmuebles.models import Inmueble
from apps.inmuebles.forms import InmuebleForm
# Create your views here.
def inmuebles(request):
	#return HttpResponse("holadola caracola")
	inmueble_tot = Inmueble.objects.all()
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