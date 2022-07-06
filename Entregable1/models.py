from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null = True)
    ocupacion = models.CharField(max_length=30)
    
    def __str__(self):
        return f'Soy {self.nombre} tengo {self.edad} años, nací el {self.fecha_nacimiento} y soy {self.ocupacion}'