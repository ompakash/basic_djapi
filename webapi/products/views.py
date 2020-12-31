from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

from .models import products 
from .serializers import productsSerializers
#the name of app is products
#the name of serializers is serializers


@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        obj = products.objects.all()
        #serializer
        serializer = productsSerializers(obj, many = True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = productsSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def product_detail(request,pk):
    try:
        obj = products.objects.get(id = pk)
    except products.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET': 
        serializer = productsSerializers(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = productsSerializers(obj,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAT_REQUEST)        