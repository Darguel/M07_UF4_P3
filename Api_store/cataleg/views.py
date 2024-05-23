from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProducteSerializer
from .models import Producte

@api_view(['GET'])
def producte_list(request):
    productes = Producte.objects.all()
    serializer = ProducteSerializer(productes, many=True)
    return Response({"data":serializer.data})

@api_view(['GET'])
def producte_detail(request, pk):
    producte = Producte.objects.get(pk=pk)
    serializer = ProducteSerializer(producte)
    return Response({"data":serializer.data})

@api_view(['POST'])
def producte_create(request):
    serializer = ProducteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"data":serializer.data})

@api_view(['PUT'])
def producte_update(request,pk):

    producte = Producte.objects.get(id=pk)

    producte.nomProducte = request.data['nomProducte']
    producte.descripcio = request.data['descripcio']
    producte.preu = request.data['preu']
    producte.stock = request.data['stock']
    producte.marcat = request.data['marcat']

    producte.save()

    serializer = ProducteSerializer(producte)
    return Response({"data":serializer.data})

@api_view(['PUT'])
def producte_update_stock(request,pk):
    producte = Producte.objects.get(id=pk)
    producte.stock = request.data['stock']
    producte.save()

    serializer = ProducteSerializer(producte)

    return Response({"data":serializer.data})

@api_view(['PUT'])
def producte_delete(request,pk):
    producte = Producte.objects.get(id=pk)
    producte.marcat = True
    producte.save()

    serializer = ProducteSerializer(producte)

    return Response({"data":serializer.data})
