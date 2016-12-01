from __future__ import unicode_literals

from django.db import models
from Location.models import *
from Category.models import *
from django.contrib.auth.models import User


# Create your models here.


class ShopTable(User):
    usertype = models.CharField(max_length=20)
    shop = models.CharField(max_length=250)
    category = models.ForeignKey(MainCategoryTable)
    details = models.CharField(max_length=1000, null=True)
    contact = models.CharField(max_length=10, null=True)
    location = models.ForeignKey(LocationTable)
    gcm_token = models.CharField(max_length=1000, null=True, blank=True)
    
    def __unicode__(self):
        return unicode(self.shop)