from django.conf.urls import include, url

from apps.propietarios.views import propietarios

urlpatterns = [
    url(r'^$', propietarios),
]
