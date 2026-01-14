from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def listaestudiantes(request):
    return render(request , 'estudiantes/listaestudiante.html')


