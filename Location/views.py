from django.shortcuts import render
from Location.models import *
from Location.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class LocationView(APIView):
    def get(self, request, format=None):
        locations = LocationTable.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)