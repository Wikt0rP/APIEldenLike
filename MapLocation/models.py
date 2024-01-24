from django.db import models


class MapLocation(models.Model):

    locationName = models.CharField(max_length=100)
    discovered = models.BooleanField(default=False)
    locationDescription = models.CharField(max_length=100, null=True, blank=True)

