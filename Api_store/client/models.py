from django.db import models

class client(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100)
    cognoms=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.nom
    
