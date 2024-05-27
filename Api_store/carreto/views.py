from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProducteSerializer
from .serializer import CarretoItemSerializer
from .models import carreto
from .models import ItemCarreto
from .models import Producte

@api_view(['GET'])
def carreto_list(request):
    carretos = carreto.objects.all()
    serializer = ProducteSerializer(carretos, many=True)
    return Response({"data":serializer.data})

@api_view(['GET'])
def productesCarreto_list(request,pk):
    productesCarreto = ItemCarreto.objects.get(carreto_id=pk)
    serializer = CarretoItemSerializer(productesCarreto)
    return Response({"data":serializer.data})

@api_view(['POST'])
def carreto_create(request):
    serializer = ProducteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"data":serializer.data})


#Para actualizar solo necesitas cantidad i buscar el producte id aparte de 
@api_view(['PUT'])
def carreto_addProducte(request,pk):

    productesCarreto = ItemCarreto.objects.get(carreto_id=pk)
    
    producte = Producte.objects.get(id = request.data['producte_id'])

    productesCarreto.quantitat = request.data['quantitat'] 

    productesCarreto.save()

    serializer = ProducteSerializer(productesCarreto)
    return Response({"data":serializer.data})