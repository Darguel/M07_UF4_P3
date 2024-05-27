from rest_framework import serializers
from .models import carreto
from .models import ItemCarreto

class ProducteSerializer(serializers.ModelSerializer):
    class Meta:
        model = carreto
        fields = '__all__'
        
class CarretoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarreto
        fields = '__all__'