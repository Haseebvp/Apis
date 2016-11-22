from django.shortcuts import render
from Category.models import *
from Category.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class MainCategoryview(APIView):
    def get(self, request, format=None):
        maincategories = MainCategoryTable.objects.all()
        serializer = MainCategorySerializer(maincategories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MainCategorySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        maincategories = self.get_object(pk)
        maincategories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Categoryview(APIView):
    def get(self, request, format=None):
        categories = CategoryTable.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categories = self.get_object(pk)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubCategoryview(APIView):
    def get(self, request, format=None):
        subcategories = SubCategoryTable.objects.all()
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubCategorySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categories = self.get_object(pk)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SingleCategory(APIView):
    def get(self, request, pk, format=None):
        category = CategoryTable.objects.filter(maincategory=pk)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

class SingleSubCategory(APIView):
    def get(self, request, pk, format=None):
        subcategory = SubCategoryTable.objects.filter(category=pk)
        serializer = SubCategorySerializer(subcategory, many=True)
        return Response(serializer.data)



