#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hola mundo!")
