from django.db import models
from Studenti.models import *
from Materie.models import  *
""" modello che rappresenta un documento pdf"""

class DocumentoPDF(models.Model):
    nome=models.CharField(max_length=255)
    file_pdf = models.BinaryField()
    def __str__(self):
        return f"{self.nome}"


class Appunto(models.Model):
    docpdf = DocumentoPDF
    voto_medio=models.IntegerField()  #attributo derivato
    Num_scaricamento=models.IntegerField() #attributo derivato
    studente=models.ForeignKey(Studente, null=True, on_delete=models.SET_NULL)
    materia=models.ForeignKey(Materia, null=True, on_delete=models.SET_NULL)
    data_caricamento=models.DateTimeField()
    def __str__(self):
        return f"{self.nome} {self.studente.nome} {self.materia}"



"""dati sullo scaricamento degli Appunti"""
class Scarica(models.Model):
    studente=models.ForeignKey(Studente, null=True, on_delete=models.SET_NULL)
    appunto=models.ForeignKey(Appunto, null=True, on_delete=models.SET_NULL)
    data_scaricamento=models.DateTimeField()
    voto_assegnato=models.IntegerField(null=True)
    def __str__(self):
        return f"{self.studente.nome} {self.data_scaricamento} {self.voto_assegnato}"


""" dati sulla recenzione di un appunto da uno studente"""
class Recenzione(models.Model):
    studente=models.ForeignKey(Studente,null=True, on_delete=models.SET_NULL)
    appunto=models.ForeignKey(Appunto, null=True, on_delete=models.SET_NULL)
    data_recenzione= models.DateTimeField()
    Testo_recenzione= models.CharField(max_length=200)
    def __str__(self):
        return f"{self.studente.nome} {self.data_scaricamento} {self.voto_assegnato}"


""" dati sulla cancellazione degli Appunti da uno studente """
class Cancella(models.Model):
    appunto=models.ForeignKey(Appunto, null=True, on_delete=models.SET_NULL)
    studente= models.ForeignKey(Studente, null=True, on_delete=models.SET_NULL)
    data_cancellazione=models.DateTimeField()
    def __str__(self):
        return f"{self.appunto.docpdf.nome} {self.studente.nome} {self.data_cancellazione}"

# Create your models here.
