from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


#def greet(request,nome):
#    return render(request, "greet.html", {'name': nome})

def bomdia(request, nome):
    agora = datetime.now()
    dia = agora.hour < 18
    dia = agora < 12
    return render(request, 'tia_do_zap.html', {'name':nome, 'dia': False})