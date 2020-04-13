#-*- coding: utf-8 -*-

from django.db import models


class Canal(models.Model):
    class Meta:
        pass

    nombre = models.CharField(max_length=100, unique=True)
    icono = models.CharField(max_length=500, default='images/iconos/default.png')
    posicion = models.IntegerField(unique=True)



