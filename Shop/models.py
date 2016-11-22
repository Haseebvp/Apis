from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ShopTable(models.Model):
    name = models.CharField(max_length=250)
    
    def __unicode__(self):
        return unicode(self.name)