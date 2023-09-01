from django.db import models


# Create your models here.
"""dati sugli Studenti"""
class Studente(models.Model):
    nome=models.CharField(max_length=100)
    cognome=models.CharField(max_length=100)
    dataNascita=models.DateField()
    password=models.CharField(null=True, max_length=255)
    email = models.EmailField(null=True, max_length=100)
    def __str__(self):
        return f"{self.nome} {self.cognome} {self.dataNascita}"

# Create your models here.
