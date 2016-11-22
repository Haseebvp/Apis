from rest_framework import serializers
from django.conf import settings
from Shop.models import *


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopTable
        fields = ('id', 'name')



