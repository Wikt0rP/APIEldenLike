from django.db import models


class Weapon(models.Model):
    weaponName = models.CharField(max_length=100, null=False, blank=False)
    weaponDescription = models.CharField(max_length=100, null=False, blank=False)
    weaponPrice = models.IntegerField(null=False, blank=False)
    weaponAttack = models.IntegerField(null=False, blank=False)
    weaponAttackSpeed = models.IntegerField(null=False, blank=False)
