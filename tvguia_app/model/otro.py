#-*- coding: utf-8 -*-

from django.db import models

from .programa import Programa


class Otro(Programa):
    class Meta:
        pass

    titulo = models.CharField(max_length=100, unique=True)
    duracion = models.IntegerField(null=True)
    imagen = models.CharField(max_length=500, null=True)

