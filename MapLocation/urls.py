from django.contrib import admin
from django.urls import path
from MapLocation import views

urlpatterns = [
    path('location/create', views.CreateLocation.as_view()),
    path('location/list', views.ListLocations.as_view()),

]
