from django.db import models
from carreto.models import carreto

class Comanda(models.Model):
    carreto = models.ForeignKey(carreto, on_delete=models.CASCADE)
    total_productes = models.PositiveIntegerField()
    preu_total = models.DecimalField(max_digits=10, decimal_places=2)
    estat = models.CharField(max_length=20, default='oberta')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)