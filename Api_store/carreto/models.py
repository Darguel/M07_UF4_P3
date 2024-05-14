from django.db import models
from client.models import client
from cataleg.models import Producte

class carreto(models.Model):
    client = models.OneToOneField(client, on_delete=models.CASCADE)
    estat = models.CharField(max_length=20, default='obert')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class ItemCarreto(models.Model):
    carreto=models.ForeignKey(carreto,on_delete=models.CASCADE)
    Producte=models.ForeignKey(Producte,on_delete=models.CASCADE)
    quantitat=models.PositiveIntegerField(default=1)
