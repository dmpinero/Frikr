#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo

def home(request):
    photos = Photo.objects.all().order_by('-created_at') # Devuelve todas las fotos a través del ModelManager. # Se configura la query, ordenadación descentente por fecha de creación
    context = {
        'photos_list': photos[:5] # Limita la query. Sólo se ejecuta cuando la variable va a ser utilizada
    }

    return render(request, 'photos/home.html', context) # Django busca en cualquier carpeta templates de todas las aplicaciones instaladas
