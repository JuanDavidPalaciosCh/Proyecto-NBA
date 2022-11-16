from email.mime import image
from django.db import models


class Equipo(models.Model):
    id_equipo: int = models.IntegerField(default=0)
    nombre: str = models.CharField(max_length=50)
    apodo: str = models.CharField(max_length=20, default='')
    codigo: str = models.CharField(max_length=20, default='')
    ciudad: str = models.CharField(max_length=30, default='')
    escudo: image = models.ImageField()
        

    def __str__(self) -> str:
        return self.nombre 
