from django.conf.urls import include, url

from apps.inmuebles.views import inmuebles, inmueble_view

urlpatterns = [
	url(r'^index$', inmuebles, name='inmuebles'),
	url(r'^nuevo$', inmueble_view, name='inmueble_create'),
]
