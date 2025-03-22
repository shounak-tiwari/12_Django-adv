from django.shortcuts import render
from .models import Item
from rest_framework.response import Response
from .serializer import ItemSerializer
from rest_framework import status
from rest_framework.decorators import api_view




@api_view(['GET'])
def item_list(request):
    if request.method =="GET":
        items = Item.objects.all()
        obj = ItemSerializer(items,many=True)
        return Response(obj.data)


@api_view(['POST'])

def create_item(request):
    serializer_obj = ItemSerializer(data=request.data)
    if serializer_obj.is_valid():
        serializer_obj.save()
        return Response(serializer_obj.data,status = status.HTTP_201_CREATED)
    
    return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)

