from rest_framework import serializers
from django.conf import settings
from Location.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationTable
        fields = '__all__'