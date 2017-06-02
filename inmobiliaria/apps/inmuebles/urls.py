from django.conf.urls import include, url

from apps.inmuebles.views import inmuebles, inmueble_view, inmueble_edit

urlpatterns = [
	url(r'^index$', inmuebles, name='inmuebles'),
	url(r'^nuevo$', inmueble_view, name='inmueble_create'),
	url(r'^editar/(?P<id_inmueble>\d+)/$', inmueble_edit, name='inmueble_editar'),
]
