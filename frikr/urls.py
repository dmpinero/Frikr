#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from photos.views import home

urlpatterns = [
    # Administrador
    url(r'^admin/', admin.site.urls),

    # Photos URLs
    url(r'^$', home, name="photos_home"), # La URL vacía (que se define con la expresión regular r'^$' se gestiona con el
                     # método home del paquete photos.views
                     # el parámetro name permite establecer un alias para referirnos a él en las vistas
    url(r'^photos/(?P<pk>[0-9]+)$', 'photos.views.detail', name="photo_detail"), # Obtiene el id de la foto y lo pasa a un controlador
    url(r'^photos/new$', 'photos.views.create', name="photo_create"),

    # Users URLs
    url(r'^login$', 'users.views.login', name="users_login"),
    url(r'^logout$', 'users.views.logout', name="users_logout")

]
