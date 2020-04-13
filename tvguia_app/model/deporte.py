#-*- coding: utf-8 -*-

from django.db import models

from .programa import Programa


class Deporte(Programa):
    class Meta:
        pass

    titulo = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=1000, null=True)
    imagen = models.CharField(max_length=500, null=True)


