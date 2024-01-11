from django.shortcuts import render
from rest_framework import request, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from Boss.models import Boss
from Item.models import Item


# Create your views here.

class BossCreate(CreateAPIView):
    def post(self, request, *args, **kwargs):
        bossName = request.data['bossName']
        bosshp = request.data['bossHp']
        bossAttack = request.data['bossAttack']
        itemID = request.data['bossReward']
        item = Item.objects.get(pk=itemID)
        if item is not None:
            boss = Boss(bossName=bossName, bossHP=bosshp, bossAttack=bossAttack, bossReward=item)
            boss.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

