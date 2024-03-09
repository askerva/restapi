from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from carrental.models import Car

from carrental.serializer import CarSerializer

# Create your views here.

@api_view(['GET','POST','DELETE','PUT'])   
def cars(request):
    if request.method == 'GET':
        objCar = Car.objects.all()
        serializer = CarSerializer(objCar,many = True )
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = CarSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data =request.data
        obj = Car.objects.get(id = data['id'])
        serializer = CarSerializer(obj,data=data,partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
        
    else:
        data = request.data
        obj = Car.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})