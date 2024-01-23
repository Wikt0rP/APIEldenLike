from django.db import models

from Boss.models import Boss
from Item.models import Item
from Weapon.models import Weapon


class Reward(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True, blank=True)
    moneyReward = models.IntegerField(null=True, blank=True)
    bossReward = models.ForeignKey(Boss , on_delete=models.CASCADE, null=True, blank=True)