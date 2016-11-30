from __future__ import unicode_literals

from django.db import models

# Create your models here.

class LocationTable(models.Model):
    location = models.CharField(max_length=250, unique=True)
    country = models.CharField(max_length=250)
    latitude = models.CharField(max_length=500, null=True, blank=True)
    longitude = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.location)