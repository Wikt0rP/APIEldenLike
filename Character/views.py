from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Character.models import Character
from Character.serializer import CharacterSerializer
from Inventory.models import Inventory
from Stats.models import Stats


class CharacterCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CharacterSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        name = request.data['name']
        startLevel = request.data['startLevel']
        potion = 3
        stats = Stats()
        stats.save()
        inventory = Inventory()
        inventory.save()
        character = Character(characterName=name, user=user, level=startLevel, money=0, potion=potion, stats=stats, inventory=inventory)
        character.save()
        return Response(status=status.HTTP_201_CREATED)


class CharacterList(generics.ListAPIView):
    queryset = Character
    serializer_class = CharacterSerializer

    def get(self, request, *args, **kwargs):
        character = Character.objects.all()
        serializer = CharacterSerializer(character, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


