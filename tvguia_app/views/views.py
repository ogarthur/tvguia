from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

from datetime import datetime,timedelta
from ..model.programa import Programa
from ..model.canal import Canal
import json


def index(request, dia="hoy"):
    """  MAIN PAGE """
    now = datetime.now()
    hoy = now.strftime("%d")
    hora_actual = now.strftime("%H:i")
    '''dev comment'''

    hoy = '14'
    if dia == "hoy":
        fecha_min = datetime.strptime(now.strftime("%Y/%m/%d"),"%Y/%m/%d")

        fecha_max = fecha_min + timedelta(days=2)
        canales = Canal.objects.all();
        canales_json = list(Canal.objects.all().values());

        for canal in canales_json:

            cartelera = Programa.objects.filter(hora_inicio__range=(fecha_min, fecha_max),
                                                canal_emision_id=canal['id']).values().order_by('hora_inicio')

            canal['programacion'] = list(cartelera)
            print(list(cartelera))

        return render(request, 'tvguia_app/home.html', {'panel': canales_json,'hora_actual': hora_actual})
    else:

        return render(request, 'tvguia_app/home.html')

def about(request):
    """  MAIN PAGE """
    return render(request, 'tvguia_app/about.html')