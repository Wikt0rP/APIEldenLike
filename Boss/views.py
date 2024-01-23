from django.shortcuts import render
from rest_framework import request, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from Boss.models import Boss
from Item.models import Item
from Reward.models import Reward


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


class BossList(CreateAPIView):
    def get(self, request, *args, **kwargs):
        boss = Boss.objects.all()
        return Response(boss.values(), status=status.HTTP_200_OK)


class BossDetail(CreateAPIView):
    def get(self, request, *args, **kwargs):
        bossID = request.data['bossID']
        boss = Boss.objects.get(pk=bossID)
        return Response(boss.values(), status=status.HTTP_200_OK)


class BossDrop(CreateAPIView):
    def get(self, request, *args, **kwargs):
        bossID = request.data['bossID']
        boss = Boss.objects.get(pk=bossID)

        rewardID = Reward.objects.get(pk=boss.bossReward.pk)
        reward = Reward.objects.get(pk=rewardID)

        return Response(reward.values(), status=status.HTTP_200_OK)
