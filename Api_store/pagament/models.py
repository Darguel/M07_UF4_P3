from django.db import models
from comandes.models import Comanda

class Pagament(models.Model):
    comanda = models.OneToOneField(Comanda, on_delete=models.CASCADE)
    numero_tarjeta = models.CharField(max_length=16)
    data_caducitat = models.DateField()
    cvc = models.CharField(max_length=3)
    estat = models.CharField(max_length=20, default='pendent')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
