from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ClientSerializer
from .models import client

@api_view(['POST'])
def client_create(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"data":serializer.data})