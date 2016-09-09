#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from users.forms import LoginForm

def login(request):
    error_messages = []
    if request.method == "POST":
        form = LoginForm(request.POST)  # Instanciar el formulario de Django
        if form.is_valid():
            username = form.cleaned_data.get("usr") # Acceder a datos una vez "limpiados" (quitado espacios en blanco, etc.)
            password = form.cleaned_data.get("pwd") # Acceder a datos una vez "limpiados" (quitado espacios en blanco, etc.)
            user = authenticate(username=username, password=password) # Encripta la password que le pasamos y la busca en
                                                                      # la base de datos
            if user is None:
                error_messages.append("Nombre de usuario o contraseña incorrectos")
            else:
                if user.is_active:
                    django_login(request, user) # Autenticar al usuario en el sistema
                    return redirect('photos_home')
                else:
                    error_messages.append("El usuario no está activo")
    else:
        form = LoginForm() # Inicialización cuando el formulario es por GET
    context = {
        'errors': error_messages,
        'login_form': form
    }

    return render(request, 'users/login.html', context)

def logout(request):
    # si el usuario está autenticado se quita la autenticación
    if request.user.is_authenticated():
        django_logout(request)

    return redirect('photos_home')
