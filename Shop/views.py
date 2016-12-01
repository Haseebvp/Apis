from django.shortcuts import render

# Create your views here.
from Shop.models import *
from Shop.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.renderers import JSONRenderer
import requests
from rest_framework import status
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from Users.UserAuth import CustomView
import pdb


# Create your views here.

def get_session_id(request):
    if not request.session.session_key:
        request.session.cycle_key()
    return request.session.session_key

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




class SignUp(CustomView):
    def auth_login(self, data):
        print 'first',data
        user = authenticate(**data)
        print 'second',user
        if user is not None:
            login(self.request, user)
            return True
            # Redirect to a success page.

        else:
            return False

    def post(self, request, format=None):
        print request.data
        serializer = ShopSerializer(data=request.data)
        if not serializer.is_valid():
            print 'validity check : ',serializer.errors
            return self.send_response(0, {'error': serializer.errors})
        else:
            print 'else validity check'
            query = serializer.validated_data
            user = ShopTable()
            user.username = query['username']
            user.usertype = query['usertype']
            user.shop = query['shop']
            user.category = query['category']
            user.details = query['details']
            user.contact = query['contact']
            user.location = query['location']
            user.set_password(query['password'])
            user.save()
            if self.auth_login({'username': query['username'], 'password': query['password']}):
                print 'login check'
                authuser = ShopTable.objects.get(username=query['username'])
                return self.send_response(1, {'session':get_session_id(request), 'completed':True, 'id':authuser.id, 'usertype':authuser.usertype})
        return self.send_response(0, {'data': serializer.errors})



class Login(CustomView):

    def auth_login(self, data):
        print 'first',data
        user = authenticate(**data)
        print 'second',user
        if user is not None:
            login(self.request, user)
            return True
        else:
            return False

    def post(self, request, format=None):
        print request.data
        if request.user.is_authenticated():
            print 'logout'
            logout(request)
            pass
        serializer = LoginUserSerializer(data=request.data)
        if not serializer.is_valid():
            print 'validity check'
            return self.send_response(0, {'error':"There is an error it seems!"})
        else:
            query = serializer.validated_data
            print 'else validity check'
            if self.auth_login({'username': query['username'], 'password': query['password']}):
                user = ShopTable.objects.get(username=query['username'])
                print 'login check'
                return self.send_response(1, {'session_id':get_session_id(request), 'completed':True, 'id':user.id, 'usertype':authuser.usertype})
            else:
                return self.send_response(0, {'error':"There is an error it seems!"})
        return self.send_response(0, {'error':"There is an error it seems!"})




class UserQuery(CustomView):

    def post(self, request, format=None):
        print request.data,"====",request.user
        serializer = QuerySerializer(data=request.data)
        if not serializer.is_valid():
            print 'validity check'
            return self.send_response(0, {'error':"There is an error it seems!"})
        else:
            query = serializer.validated_data
            print 'else validity check'

            return self.send_response(1, {'data':"success"})
        return self.send_response(0, {'error':"There is an error it seems!"})


