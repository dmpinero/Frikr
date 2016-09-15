#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo, PUBLIC
from photos.forms import PhotoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

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
    possible_photos = Photo.objects.filter(pk=pk).select_related('owner') # Django busca por la clave primaria, sin importar el campo que sea
    photo = possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        # Cargar la plantilla de detalle
        context = {
            'photo': photo
        }

        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound("No existe la foto") # 404 Not found

@login_required()
def create(request):
    """
    Muestra un formulario para crear una foto. La crea si la petición es POST
    :param request: HttpRequest
    :return: HttpResponse
    """
    success_message = ""
    form = PhotoForm()
    if request.method == "GET":
        form = PhotoForm()
    else:
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user # Propietario de la foto: Usuario autenticado
        form = PhotoForm(request.POST, instance=photo_with_owner) # Le pasamos como instancia la Foto que le pasamos por parámetro
        if form.is_valid():
            new_photo = form.save() # Guarda el objeto y lo devuelve
            form = PhotoForm()      # Inicializa el formulario y lo devuelve vacío (en la plantilla se mostrará el
                                    # formulario vacío
            success_message = 'Guardado con éxito!' # Mensaje de foto creada con éxito
            success_message += '<a href="{0}">'.format(reverse('photo_detail', args=[new_photo.pk])) # Reverse monta una URL. args son los argumentos de la URL.
            success_message += 'Ver foto'
            success_message += "</a>"

    context = {
        'form': form,
        'success_message': success_message
    }

    return render(request, 'photos/new_photo.html', context)