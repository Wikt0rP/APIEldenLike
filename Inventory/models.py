from django.db import models

from Character.models import Character
from Item.models import Item


class Inventory(models.Model):
    itemInventory = models.ManyToManyField(Item, blank=True, related_name='itemInventory')
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='characterInventory')

