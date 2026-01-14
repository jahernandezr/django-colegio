from django.shortcuts import render

def litasdecursos(request):
    return render(request , 'cursos/listarcursos.html')
