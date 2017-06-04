from django.conf.urls import include, url

from apps.inmuebles.views import inmueble_view, inmueble_edit, \
	Inmuebles, inmueble_delete

urlpatterns = [
	url(r'^index$', Inmuebles.as_view(), name='inmuebles'),
	url(r'^nuevo$', inmueble_view.as_view(), name='inmueble_create'),
	url(r'^editar/(?P<pk>\d+)/$', inmueble_edit.as_view(), name='inmueble_editar'),
	url(r'^delete/(?P<pk>\d+)/$', inmueble_delete.as_view(), name='inmueble_editar'),
]
