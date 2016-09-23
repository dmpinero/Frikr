#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from photos.models import Photo
from photos.settings import PROJECT_BADWORDS

class PhotoForm(forms.ModelForm):
    """
    Formulario para el modelo Photo
    """
    class Meta:
        model = Photo
        exclude = ['owner'] # Campos que no queremos que pinte

