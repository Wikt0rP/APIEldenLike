from django.contrib import admin
from django.urls import path
from Reward import views

urlpatterns = [
    path('reward/add', views.RewardAdd.as_view()),
    path('reward/list', views.RewardAdd.as_view()),

]
