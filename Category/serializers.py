from rest_framework import serializers
from django.conf import settings
from Category.models import *


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategoryTable
        fields = ('id', 'name', 'image')



class CategorySerializer(serializers.ModelSerializer):
    maincategory = serializers.SerializerMethodField()
    
    def get_maincategory(self, object):
        return MainCategorySerializer(object.maincategory).data

    class Meta:
        model = CategoryTable
        fields = ('id', 'name', 'image', 'maincategory')   
       

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    
    def get_category(self, object):
        return CategorySerializer(object.category).data

    class Meta:
        model = SubCategoryTable
        fields = ('id', 'name', 'features', 'shop_type', 'category')   
       


