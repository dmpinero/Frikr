#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

# getattr devuelve el atributo LICENSES del archivo settings.py del proyecto. Si no lo encuentra devuelve el valor de DEFAULT_LICENSES
LICENSES = getattr(settings, 'LICENSES', DEFAULT_LICENSES)

# Tacos no permitidos
PROJECT_BADWORDS = getattr(settings, 'BADWORDS', [])