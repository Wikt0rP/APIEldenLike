from django.contrib import admin
from django.urls import path
from Item import views

urlpatterns = [
    path('item/create', views.ItemCreate.as_view()),
    path('item/list', views.ItemList.as_view()),
]
