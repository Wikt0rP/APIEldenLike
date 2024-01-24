from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
from MapLocation.serializer import MapLocation


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
        serializer = MapLocation(locations, many=True)
        return Response(serializer.data, status=200)
    