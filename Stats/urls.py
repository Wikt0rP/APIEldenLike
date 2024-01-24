from django.contrib import admin
from django.urls import path
from Stats import views

urlpatterns = [
    path('stats/edit', views.StatsEdit.as_view()),
    path('stats/list', views.StatsList.as_view()),

]
