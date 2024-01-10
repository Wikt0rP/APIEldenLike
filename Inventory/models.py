from django.db import models
from Item.models import Item


class Inventory(models.Model):
    itemInventory = models.ManyToManyField(Item, blank=True, related_name='itemInventory')
    weaponInventory = models.ManyToManyField(Item, blank=True, related_name='weaponInventory')
