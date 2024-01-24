from django.contrib import admin
from django.urls import path
from Inventory import views

urlpatterns = [

    path('inventory/addItem', views.InventoryAddItem.as_view()),
    path('inventory/user', views.GetUserInventory.as_view()),
    path('inventory/list', views.ListAllInventories.as_view()),
    path('inventory/create', views.CreateInventory.as_view()),
]
