#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login

def login(request):
    error_messages = []
    if request.method == "POST":
        username = request.POST.get("usr")
        password = request.POST.get("pwd")

        user = authenticate(username=username, password=password) # Encripta la password que le pasamos y la busca en
                                                                  # el usuario de la base de datos
        if user is None:
            error_messages.append("Nombre de usuario o contraseña incorrectos")
        else:
            if user.is_active:
                django_login(request, user) # Autenticar al usuario en el sistema
                return redirect('photos_home')
            else:
                error_messages.append("El usuario no está activo")

    context = {
        'errors': error_messages
    }

    return render(request, 'users/login.html', context)

def logout(request):
    # si el usuario está autenticado se quita la autenticación
    if request.user.is_authenticated():
        django_logout(request)

    return redirect('photos_home')
