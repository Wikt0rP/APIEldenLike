from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from MapLocation.models import MapLocation
# Create your views here.
from MapLocation.serializer import MapLocationSerializer


class CreateLocation(APIView):
    def post(self, request):
        locationName = request.data['locationName']
        locationDescription = request.data['locationDescription']
        location = MapLocation(locationName=locationName, locationDescription=locationDescription)
        location.save()
        return Response(status=201)


class ListLocations(APIView):
    queryset = MapLocation
    serializer_class = MapLocation

    def get(self, request):
        locations = MapLocation.objects.all()
        serializer = MapLocationSerializer(locations, many=True)
        return Response(serializer.data)
    