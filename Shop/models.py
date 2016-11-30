from __future__ import unicode_literals

from django.db import models
from Location.models import *

# Create your models here.


class ShopTable(models.Model):
    shop = models.CharField(max_length=250)
    shop_type = models.CharField(max_length=250, null=True)
    details = models.CharField(max_length=1000, null=True)
    contact = models.CharField(max_length=10, null=True)
    location = models.ForeignKey(LocationTable)
    
    def __unicode__(self):
        return unicode(self.shop)