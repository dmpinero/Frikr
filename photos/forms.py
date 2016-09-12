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

        def clean(self):
            """
            Valida si en la descripción se han puesto tacos definidos en settings.BADWORDS
            :return: diccionario con los atributos si OK
            """
            cleaned_data = super(PhotoForm ,self).clean() # Recupera del formulario los datos "limpiados" por el padre
            description = cleaned_data.get('description', '')

            for badword in PROJECT_BADWORDS:
                if badword.lower() in description.lower():
                    raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

            # Si todo va OK, devuelvo los datos limpios/normalizados
            return cleaned_data
