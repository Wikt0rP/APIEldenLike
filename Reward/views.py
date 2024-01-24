from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from Boss.models import Boss
from Reward.models import Reward
from Reward.serializer import RewardSerializer


# Create your views here.

class RewardAdd(APIView):
    def post(self, request):
        name = request.data['rewardName']
        description = request.data['rewardDescription']
        bossID = request.data['rewardBoss']
        money = request.data['moneyReward']
        rewardBoss = Boss.objects.get(pk=bossID)

        reward = Reward(rewardName=name, rewardDescription=description, moneyReward= money,rewardBoss=rewardBoss)
        reward.save()
        return Response(status=201)


class RewardList(APIView):
    queryset = Reward
    serializer_class = RewardSerializer

    def get(self, request):
        rewards = Reward.objects.all()
        serializer = self.serializer_class(rewards, many=True)
        return Response(serializer.data, status=200)