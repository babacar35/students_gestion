from django.db import models

# Create your models here.
class Student(models.Model):
    matricule = models.PositiveIntegerField()
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    domaine_etude = models.CharField(max_length=100)
    gpa = models.FloatField()
    def __str__(self) -> str:
        return f'Student : {self.prenom} {self.nom}'

