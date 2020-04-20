from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.utils import timezone

from datetime import datetime, timedelta
from ..model.programa import Programa
from ..model.canal import Canal
import json


def index(request, dia="hoy"):
    """  MAIN PAGE """
    now = timezone.now()
    hoy = now.strftime("%d")
    hora_actual = now.strftime("%H:i")
    '''dev comment'''

    hoy = '14'
    if dia == "hoy":
        fecha_min = datetime.strptime(now.strftime("%Y/%m/%d"), "%Y/%m/%d")

        fecha_max = fecha_min + timedelta(days=2)
        canales = Canal.objects.all();
        canales_json = list(Canal.objects.all().values());

        for canal in canales_json:
            cartelera = Programa.objects.filter(hora_inicio__range=(fecha_min, fecha_max),
                                                canal_emision_id=canal['id']).values().order_by('hora_inicio')

            canal['programacion'] = list(cartelera)
            print(list(cartelera))

        return render(request, 'tvguia_app/home.html', {'panel': canales_json, 'hora_actual': hora_actual})
    else:

        return render(request, 'tvguia_app/home.html')


def fill(request):
    now = datetime.now()
    # {'nombre': , 'icono': , 'posicion': }
    canales = [{'nombre': "tve1", 'icono': 'tve1.webp', 'posicion': "1"},
               {'nombre': "tve2", 'icono': 'tve2.webp', 'posicion': "2"},

               ]
    programas = [
        {
        'hora_inicio': now,
        'hora_fin': now + timedelta(hours=2),
        'titulo':"Pear Harbor",
        'descripcion':"pelicula belica sobre el ataque sorpresa de pear harbor",
        'imagen':"poster1.jpg",
        'tipo':"pelicula",
        'canal_emision': "tve1"
        },
    {
        'hora_inicio': now - timedelta(hours=2),
        'hora_fin': now,
        'titulo':"starshiptroopers",
        'descripcion':"guerra de arañas",
        'imagen':"poster2.jpg",
        'tipo':"pelicula",
        'canal_emision':"tve1"
    },
    {
        'hora_inicio': now+ timedelta(hours=2),
        'hora_fin': now + timedelta(hours=3),
        'titulo':"seriesinimage",
        'descripcion': "prueba",
        'imagen': "poster1.jpg",
        'tipo':"serie",
        'canal_emision':"tve2"
    }
    ]




    # INSERTAR CANALES
    canal_bulk = []
    for canal in canales:
        if not Canal.objects.filter(nombre=canal['nombre']).exists():
            new_canal = Canal()
            new_canal.nombre = canal['nombre']
            new_canal.icono = canal['icono']
            new_canal.posicion = canal['posicion']
            canal_bulk.append(new_canal)
    Canal.objects.bulk_create(canal_bulk)

    # INSERTAR PROGRAMAS
    programa_bulk = []
    for programa in programas:
        new_programa = Programa()
        new_programa.hora_inicio = programa['hora_inicio']
        new_programa.hora_fin = programa['hora_fin']
        new_programa.titulo = programa['titulo']
        new_programa.descripcion = programa['descripcion']
        new_programa.imagen = programa['imagen']
        new_programa.tipo = programa['tipo']
        new_programa.canal_emision = Canal.objects.get(nombre=programa['canal_emision'])
        programa_bulk.append(new_programa)
    Programa.objects.bulk_create(programa_bulk)
    return render(request, 'tvguia_app/home.html')


def about(request):
    """  MAIN PAGE """
    return render(request, 'tvguia_app/about.html')
