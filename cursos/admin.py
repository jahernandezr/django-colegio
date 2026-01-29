from django.contrib import admin
from .models import cursos, materias,tipo_cursos,tipo_jornada

# Register your models here.

admin.site.register(cursos)
admin.site.register(materias)
admin.site.register(tipo_cursos)
admin.site.register(tipo_jornada)
