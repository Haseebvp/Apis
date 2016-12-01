from rest_framework import serializers
from django.conf import settings
from Shop.models import *


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopTable
        fields = '__all__'


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)


class QuerySerializer(serializers.Serializer):
    category = serializers.CharField(max_length=30)
    query = serializers.CharField(max_length=500)
    location = serializers.CharField(max_length=30)



