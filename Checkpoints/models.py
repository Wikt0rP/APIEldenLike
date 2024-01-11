from django.db import models


class Checkpoints(models.Model):
    checkpointName = models.CharField(max_length=100)
    checkpointX = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    checkpointY = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    checkpointZ = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    checkpointReached = models.BooleanField(default=False)