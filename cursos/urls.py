from django.urls import path
from . import  views

urlpatterns =[
    path('listar', views.litasdecursos , name='listas-cursos'),
    path('editar/<int:id>',views.editarcursos , name="editar-curso"),
    path('eliminar/<int:id>',views.deletecurso ,  name="delete-curso"),
    path('agregar', views.agregarcursos , name="agregar-curso"),
]
