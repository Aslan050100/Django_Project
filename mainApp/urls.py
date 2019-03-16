from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),

    url(r'^login', include('django.contrib.auth.urls')),
]