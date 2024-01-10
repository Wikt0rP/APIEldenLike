from django.db import models
from Item.models import Item


class Boss(models.Model):
    bossName = models.CharField(max_length=100, null=False, blank=False)
    bossHP = models.IntegerField(null=False, blank=False)
    bossAttack = models.IntegerField(null=False, blank=False)
    bossReward = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, blank=False)

