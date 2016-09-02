#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

class Photo(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True) # Incluye automáticamente la fecha y hora actuales al crear el objeto
    modified_at = models.DateTimeField(auto_now=True)    # Incluye la fecha y horas actuales al actualizar
    license = models.CharField(max_length=3, choices=LICENSES)

    # Descripción del objeto como cadena
    def __unicode__(self):
        return self.name
