from django.shortcuts import render
import requests
from rest_framework import status
from Users.models import *
from django.http import HttpResponseRedirect, JsonResponse
from Users.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class Userview(APIView):
    def get(self, request, format=None):
        users = AuthUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
    	print request.POST
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetUserview(APIView):
    def get(self, request, pk, format=None):
        user = AuthUser.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)