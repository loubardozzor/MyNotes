from django.db import models
# Create your models here.

"""dati sulle Materie della Laurea triennale in ingegneria
ingegneria informatica"""

class Materia(models.Model):
    nome=models.CharField(max_length=100)
    codMat=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome} {self.codMat}"

