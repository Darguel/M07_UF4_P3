from django.db import models

class Producte(models.Model):
    id=models.AutoField(primary_key=True)
    nomProducte = models.CharField(max_length=100)
    descripcio = models.TextField()
    preu = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    marcat = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.nomProducte

