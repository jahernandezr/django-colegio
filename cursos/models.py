from django.db import models

# Create your models here.
class cursos(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad_alumnos = models.IntegerField()
    tipo_curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class materias(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=20)
    id_colegio = models.IntegerField()

    def __str__(self):
        return self.nombre    
