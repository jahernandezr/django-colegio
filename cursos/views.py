from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from . models  import cursos
from django.contrib.auth.decorators import login_required

@login_required
def litasdecursos(request):
    curso_lista= cursos.objects.all()
    data= {
        'cursos': curso_lista
    }
    return render(request , 'cursos/listarcursos.html',data)

def editarcursos(request,id):
    curso = get_object_or_404(cursos, id=id)
    data ={
        'curso' :curso
    }
        
    if request.method == 'POST':
        curso.nombre = request.POST['nombre']
        curso.cantidad_alumnos = request.POST['cantidad_alumnos']
        curso.tipo_curso = request.POST['tipo_curso']
        curso.save()
        return  redirect('listas-cursos')
    
    return render(request, 'cursos/editar.html',data)

def deletecurso(request, id):
    curso =  get_object_or_404(cursos, id=id)
    curso.delete()

    return redirect('listas-cursos')

def agregarcursos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad_alumnos')
        tipo = request.POST.get('tipo_curso')

        if not nombre or not cantidad or not tipo:
            return render(request, 'cursos/agregar.html',{'error :' : 'Digitar todos los campos'})
        
        cursos.objects.create(
            nombre = nombre,
            cantidad_alumnos = int (cantidad) ,
            tipo_curso = tipo
        )

        return redirect('listas-cursos')
    return render(request , 'cursos/agregar.html' )

        
