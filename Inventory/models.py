from django.db import models
from Character.models import Character
from Item.models import Item


class Inventory(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    itemInventory = models.ManyToManyField(Item, blank=True, related_name='itemInventory')
    weaponInventory = models.ManyToManyField(Item, blank=True, related_name='weaponInventory')