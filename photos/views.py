#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo, PUBLIC
from photos.forms import PhotoForm

def home(request):
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at') # Devuelve todas las fotos a través del ModelManager. # Se configura la query, ordenadación descentente por fecha de creación
    context = {
        'photos_list': photos[:5] # Limita la query. Sólo se ejecuta cuando la variable va a ser utilizada
    }

    return render(request, 'photos/home.html', context) # Django busca en cualquier carpeta templates de todas las aplicaciones instaladas

# Recibe el identificador de la foto en la variable pk
def detail(request, pk):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpResponse
    """
    possible_photos = Photo.objects.filter(pk=pk) # Django busca por la clave primaria, sin importar el campo que sea
    photo = possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        # Cargar la plantilla de detalle
        context = {
            'photo': photo
        }

        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound("No existe la foto") # 404 Not found

def create(request):
    """
    Muestra un formulario para crear una foto. La crea si la petición es POST
    :param request: HttpRequest
    :return: HttpResponse
    """
    form = PhotoForm()
    if request.method == "GET":
        form = PhotoForm()
    else:
        form = PhotoForm(request.POST)
        if form.is_valid():
            new_photo = form.save() # Guarda el objeto y lo devuelve
            
    context = {
        'form': form
    }

    return render(request, 'photos/new_photo.html', context)