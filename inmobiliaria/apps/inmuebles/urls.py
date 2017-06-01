from django.conf.urls import include, url

from apps.inmuebles.views import inmuebles

urlpatterns = [
    url(r'^$', inmuebles),
]
