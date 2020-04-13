#-*- coding: utf-8 -*-

from django.db import models


class Programa(models.Model):
    class Meta:
        pass

    hora_inicio = models.DateTimeField(blank=True)
    hora_fin = models.DateTimeField(blank=True)


