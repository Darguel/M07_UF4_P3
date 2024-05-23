from rest_framework import serializers
from .models import client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = '__all__'