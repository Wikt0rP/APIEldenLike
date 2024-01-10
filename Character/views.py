from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Character.models import Character
from Character.serializer import CharacterSerializer
from Potion.models import Potion
from Stats.models import Stats


class CharacterCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CharacterSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        name = request.data['name']
        startLevel = request.data['startLevel']
        potion = Potion()
        stats = Stats()
        character = Character(characterName=name, user=user, level=startLevel, money=0, potion=potion, stats=stats)
        character.save()
        return Response(status=status.HTTP_201_CREATED)

