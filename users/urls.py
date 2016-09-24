#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from users.views import LoginView, LogoutView

urlpatterns = [
    # Users URLs
    url(r'^login$', LoginView.as_view(), name="users_login"),
    url(r'^logout$', LogoutView.as_view(), name="users_logout"),
]