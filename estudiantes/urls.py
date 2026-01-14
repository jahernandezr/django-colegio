from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listaestudiantes, name='lista-estudiantes')
]