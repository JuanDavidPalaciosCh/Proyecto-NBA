from django.db import models


class Jugador(models.Model):
    team_id = models.IntegerField()
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    position = models.CharField(max_length=20)
    number = models.IntegerField()

    def __str__(self) -> str:
        return self.name + " " + self.lastname
