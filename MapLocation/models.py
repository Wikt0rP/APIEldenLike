from django.db import models
from Checkpoints.models import Checkpoints


class MapLocation(models.Model):
    locationName = models.CharField(max_length=100)
    checkpoint = models.ManyToOneRel(Checkpoints, on_delete=models.CASCADE, related_name='checkpoints')
    description = models.TextField(null=True, blank=True)
