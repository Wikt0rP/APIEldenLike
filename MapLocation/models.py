from django.db import models


class MapLocation(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.data = None

    locationName = models.CharField(max_length=100)
    discovered = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

