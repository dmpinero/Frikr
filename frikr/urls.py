#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from users import urls as users_urls, api_urls as users_api_urls
from photos import urls as photos_urls, api_urls as photos_api_urls

urlpatterns = [
    # Administrador
    url(r'^admin/', admin.site.urls),
    # Users URLs
    url(r'', include(users_urls)),
    url(r'api/', include(users_api_urls)),
    # Photos URLs
    url(r'', include(photos_urls)),
    url(r'api/', include(photos_api_urls)),
]
