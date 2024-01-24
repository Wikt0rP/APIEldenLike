from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


from Stats.models import Stats


class Character(models.Model):
    characterName = models.CharField(max_length=100, null=False, blank=False)
    level = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(784)], default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    stats = models.OneToOneField(Stats, on_delete=models.CASCADE, null=False, blank=False)
    potion = models.IntegerField(null=True, blank=False, validators=[MinValueValidator(0), MaxValueValidator(15)], default=3)
    money = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(999999999)], default=0)
