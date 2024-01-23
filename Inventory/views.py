from django.shortcuts import render
from rest_framework import request, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Character.models import Character
from Inventory.models import Inventory
from Inventory.serializer import InventorySerializer
from Item.models import Item


class InventoryAddItem(CreateAPIView):
    def post(self, request, *args, **kwargs):
        itemID = request.data['itemID']
        characterID = request.data['characterID']

        if itemID is not None and characterID is not None:
            item = Item.objects.get(pk=itemID)
            character = Character.objects.get(pk=characterID)

            inventory = Inventory(itemInventory=item, character=character)
            inventory.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetUserInventory(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Character
    serializer_class = InventorySerializer

    def post(self, request, *args, **kwargs):
        characterID = request.data['characterID']

        if characterID is not None:
            character = Character.objects.get(pk=characterID)
            inventory = Inventory.objects.get(character=character)
            serializer = InventorySerializer(inventory)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ListAllInventories(CreateAPIView):
    queryset = Inventory
    serializer_class = InventorySerializer

    def get(self, request, *args, **kwargs):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)