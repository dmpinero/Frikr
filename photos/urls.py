#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from photos.views import HomeView, DetailView, CreateView

urlpatterns = [
    # Photos URLs
    url(r'^$', HomeView.as_view(), name="photos_home"), # La URL vacía (que se define con la expresión regular r'^$' se gestiona con el
                     # método home del paquete photos.views
                     # el parámetro name permite establecer un alias para referirnos a él en las vistas
    url(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name="photo_detail"), # Obtiene el id de la foto y lo pasa a un controlador
    url(r'^photos/new$', CreateView.as_view(), name="photo_create"),
]