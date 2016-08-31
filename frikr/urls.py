#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from photos.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home) # La URL vacía (que se define con la expresión regular r'^$' se gestiona con el
                     # método home del paquete photos.views
]
