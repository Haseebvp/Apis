from django.shortcuts import render

# Create your views here.
from Shop.models import *
from Shop.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.renderers import JSONRenderer

# @method_decorator(ensure_csrf_cookie)
class ShopView(APIView):
    def get(self, request, format=None):
        shop = ShopTable.objects.all()
        serializer = ShopSerializer(shop, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print request.data
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        shop = self.get_object(pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

