from django.db import models
from carreto.models import carreto

class client(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100)
    cognoms=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    carreto=models.ForeignKey(carreto, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self):
        return self.nom
    
