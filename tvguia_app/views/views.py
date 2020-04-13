from django.shortcuts import render

import json


def index(request):
    """  MAIN PAGE """
    return render(request, 'tvguia_app/home.html')

def about(request):
    """  MAIN PAGE """
    return render(request, 'tvguia_app/about.html')