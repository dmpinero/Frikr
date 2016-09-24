#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from photos.api import PhotoViewSet

# APIRouter
router = DefaultRouter()
router.register(r'api/1.0/photos', PhotoViewSet)

urlpatterns = [
    # API URLs
    url(r'1.0/', include(router.urls)), # Incluir las URLs de API
]