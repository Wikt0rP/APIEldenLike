from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Stats(models.Model):
    vigor = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(99)], default=1)
    mind = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(99)], default=1)
    endurance = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(99)], default=1)
    strength = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(99)], default=1)
    dexterity = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(99)], default=1)
    intelligence = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(99)], default=1)
    faith = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(99)], default=1)
    arcane = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(99)], default=1)