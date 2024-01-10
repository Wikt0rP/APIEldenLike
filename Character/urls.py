from django.contrib import admin
from django.urls import path
from Character import views

urlpatterns = [
    path('character/create', views.CharacterCreate.as_view()),


]
