#-*- coding: utf-8 -*-

from django.db import models

from .programa import Programa


class Noticias(Programa):
    class Meta:
        pass

    titulo = models.CharField(max_length=100, unique=True)
    duracion = models.IntegerField(null=True)
    imagen = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.titulo

