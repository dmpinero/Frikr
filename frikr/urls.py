#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from photos.api import PhotoViewSet
from photos.views import HomeView, DetailView, CreateView
from users.api import UserViewSet
from users.views import LoginView, LogoutView

# APIRouter
router = DefaultRouter()
router.register(r'api/1.0/photos', PhotoViewSet)
router.register(r'api/1.0/users', UserViewSet, base_name='user')

urlpatterns = [
    # Administrador
    url(r'^admin/', admin.site.urls),

    # Photos URLs
    url(r'^$', HomeView.as_view(), name="photos_home"), # La URL vacía (que se define con la expresión regular r'^$' se gestiona con el
                     # método home del paquete photos.views
                     # el parámetro name permite establecer un alias para referirnos a él en las vistas
    url(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name="photo_detail"), # Obtiene el id de la foto y lo pasa a un controlador
    url(r'^photos/new$', CreateView.as_view(), name="photo_create"),

    # API URLs
    url(r'', include(router.urls)), # Incluir las URLs de API

    # Users URLs
    url(r'^login$', LoginView.as_view(), name="users_login"),
    url(r'^logout$', LogoutView.as_view(), name="users_logout"),

]
