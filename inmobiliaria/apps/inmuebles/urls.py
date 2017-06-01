from django.conf.urls import include, url

from apps.inmuebles.views import index

urlpatterns = [
    url(r'^$', index),
]
