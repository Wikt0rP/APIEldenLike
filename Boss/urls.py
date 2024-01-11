from django.contrib import admin
from django.urls import path
from Boss import views

urlpatterns = [
    path('boss/create', views.BossCreate.as_view()),
    path('boss/list', views.BossList.as_view()),
    path('boss/detail', views.BossDetail.as_view()),
    path('boss/drop', views.BossDrop.as_view()),


]
