from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def propietarios(request):
	return HttpResponse("holadola caracola propietarios")