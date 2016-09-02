#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo

def home(request):
    photos = Photo.objects.all() # Devuelve todas las fotos a través del ModelManager
    html = '<ul>'
    for photo in photos:
        html += '<li>' + photo.name + '</li>'
    html += '</ul>'

    return HttpResponse(html)
