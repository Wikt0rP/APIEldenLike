from django.db import models


class Item(models.Model):
    itemName = models.CharField(max_length=100, null=False, blank=False)
    itemDescription = models.CharField(max_length=100, null=False, blank=False)
    itemPrice = models.IntegerField(null=False, blank=False)