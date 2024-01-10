from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from Stats.models import Stats


class Character(models.Model):
    characterName = models.CharField(max_length=100, null=False, blank=False)
    level = models.IntegerField(null=False, blank=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=False)
    stats = models.OneToOneField(Stats, on_delete=models.CASCADE, null=True, blank=False)

