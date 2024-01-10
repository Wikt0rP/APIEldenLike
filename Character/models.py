from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from Stats.models import Stats
from Potion.models import Potion


class Character(models.Model):
    characterName = models.CharField(max_length=100, null=False, blank=False)
    level = models.IntegerField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    stats = models.OneToOneField(Stats, on_delete=models.CASCADE, null=False, blank=False)
    potion = models.OneToOneField(Potion, on_delete=models.CASCADE, null=False, blank=False)
    money = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(999999999)], default=0)
