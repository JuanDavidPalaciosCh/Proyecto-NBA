from django.db import models


class Jugador(models.Model):
    team_id = models.IntegerField()
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    position = models.CharField(max_length=20, null=True)
    number = models.IntegerField(default=None, null=True)

    def __str__(self) -> str:
        return self.name + " " + self.lastname


    def get_position(self):
        try:
            positions = self.position.split("-")
            available_positions = {'G': 'Guarda ', 'A': 'Alero ', 'P': 'Pivot ', 'F': 'Ala-Pivot ', 'C': 'Base '}
            final_position = []
            for i in range(len(positions)):
                final_position += available_positions[positions[i]]

            final_position = "".join(final_position)
        
            return final_position
        except:
            return self.position
