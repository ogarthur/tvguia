#-*- coding: utf-8 -*-

from django.db import models

from .programa import Programa


class Serie(Programa):
    class Meta:
        pass

    titulo = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=1000, null=True)
    fecha = models.DateTimeField(blank=True)
    edad = models.IntegerField(default=0)
    puntuacion = models.IntegerField(null=True)
    duracion = models.IntegerField(null=True)
    imagen = models.CharField(max_length=500, null=True)


class Episodio(models.Model):
    class Meta:
        pass

    titulo = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=1000, null=True)
    duracion = models.IntegerField(null=True)
    numero = models.IntegerField(null=True)
    temporada = models.IntegerField(null=True)
    serie = models.ForeignKey(Serie, related_name='serie_episodio', on_delete=models.PROTECT)