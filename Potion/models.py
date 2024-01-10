from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Potion(models.Model):
    quantity = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(3), MaxValueValidator(14)], default=3)
    upgrade = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(12)], default=0)
    hpPotionQuantity = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(14)], default=3)
