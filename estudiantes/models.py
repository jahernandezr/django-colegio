from django.db import models

# Create your models here.
class estudiante(models.Model):
    nombre  = models.CharField(max_length= 50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    foto = models.ImageField(upload_to='usuario/%Y/%m/%d')

    def __str__(self):
        return self.nombre
