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
    
class tipo_cursos(models.Model):
    curso = models.CharField(max_length=30)
    activo = models.IntegerField()

    class Meta :
        db_table ='tipo_cursos'
        managed = False

    def __str__(self):
        return self.curso
    
class  tipo_jornada(models.Model):
    jornada = models.CharField(max_length=30)
    activo = models.IntegerField()

    class Meta:
        db_table ='tipo_jornada'
        managed = False

    def __str__(self):
        return self.jornada        