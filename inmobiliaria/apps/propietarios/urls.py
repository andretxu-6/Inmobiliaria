from django.conf.urls import include, url

from apps.propietarios.views import Propietarios, propietarios_view, propietarios_edit, propietarios_delete

urlpatterns = [
    url(r'^$', Propietarios.as_view(), name='listado_propietarios'),
    url(r'^nuevo$', propietarios_view.as_view(), name='propietario_create'),
    url(r'^editar/(?P<pk>\d+)/$', propietarios_edit.as_view(), name='propietario_editar'),
    url(r'^delete/(?P<pk>\d+)/$', propietarios_delete.as_view(), name='propietario_eliminar'),
]
