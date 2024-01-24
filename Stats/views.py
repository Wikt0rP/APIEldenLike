from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Character.models import Character
from Stats.models import Stats
from Stats.serializer import StatsSerializer


class StatsEdit(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StatsSerializer

    def post(self, request):
        vigor = request.data.get('vigor')
        mind = request.data.get('mind')
        endurance = request.data.get('endurance')
        strength = request.data.get('strength')
        dexterity = request.data.get('dexterity')
        intelligence = request.data.get('intelligence')
        faith = request.data.get('faith')
        arcane = request.data.get('arcane')

        characterID = request.user("characterID")
        character = Character.objects.get(pk=characterID)
        stats = Stats.objects.get(character=character)

        if vigor is not None:
            stats.vigor = vigor
        if mind is not None:
            stats.mind = mind
        if endurance is not None:
            stats.endurance = endurance
        if strength is not None:
            stats.strength = strength
        if dexterity is not None:
            stats.dexterity = dexterity
        if intelligence is not None:
            stats.intelligence = intelligence
        if faith is not None:
            stats.faith = faith
        if arcane is not None:
            stats.arcane = arcane

        stats.save()
        return Response(status=201)


class StatsList(APIView):
    queryset = Stats
    serializer_class = StatsSerializer

    def get(self, request):
        stats = Stats.objects.all()
        serializer = self.serializer_class(stats, many=True)
        return Response(serializer.data, status=200)