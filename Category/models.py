from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Category.thumbs import ImageWithThumbsField
from django.utils import timezone

def get_upload_path(instance, filename):
   return "images/" + "".join(str(timezone.now().date()).split("-")) + "/" + filename



class MainCategoryTable(models.Model):
    name = models.CharField(max_length=250)
    image = ImageWithThumbsField("Image", upload_to=get_upload_path,
                                blank=True, null=True, sizes=((100, 100), (500, 500), ("oc", "oc")))


    def __unicode__(self):
        return unicode(self.name)


class CategoryTable(models.Model):
    name = models.CharField(max_length=250)
    image = ImageWithThumbsField("Image", upload_to=get_upload_path,
                                blank=True, null=True, sizes=((100, 100), (500, 500), ("oc", "oc")))

    maincategory = models.ForeignKey(MainCategoryTable)

    def __unicode__(self):
        return unicode(self.name)

class SubCategoryTable(models.Model):
    name = models.CharField(max_length=250)
    features = models.CharField(max_length=250)
    shop_type = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryTable, default=1)


    def __unicode__(self):
        return unicode(self.name)

