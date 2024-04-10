from django.db import models

class Lignes(models.Model):
    ligneId = models.AutoField(primary_key=True)
    nom_ligne = models.CharField(max_length=200)
    start_ligne = models.CharField(max_length=200)
    end_ligne = models.CharField(max_length=200)
    depart_ligne = models.CharField(max_length=200)
    destination_ligne = models.CharField(max_length=200)
    plan_ligne = models.FileField(upload_to='plan_lignes/', null=True, blank=True)
