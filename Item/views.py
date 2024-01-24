from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Item.models import Item
from Item.serializer import ItemSerializer


# Create your views here.
class ItemCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer

    def post(self, request, *args, **kwargs):
        itemName = request.data['itemName']
        itemDescription = request.data['itemDescription']
        itemPrice = request.data['itemPrice']
        item = Item(itemName=itemName, itemDescription=itemDescription, itemPrice=itemPrice)
        item.save()
        return Response(status=status.HTTP_201_CREATED)


class ItemList(generics.ListAPIView):
    queryset = Item
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
