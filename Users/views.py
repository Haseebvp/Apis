from django.shortcuts import render
import requests
from rest_framework import status
from Users.models import *
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, Http404
from Users.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from Users.UserAuth import CustomView
import pdb


# Create your views here.

def get_session_id(request):
    if not request.session.session_key:
        request.session.cycle_key()
    return request.session.session_key

class UserDetails(CustomView):
    def get_object(self, pk):
        try:
            return AuthUser.objects.get(pk=pk)
        except AuthUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return self.send_response(1, {'data': serializer.data})

    def post(self, request, pk, format=None):
        print "DATA : ",request.data
        # pdb.set_trace()
        user = self.get_object(pk)
        # pdb.set_trace()
        print user
        serializer = UserSerializer(user, data=request.data, partial=True)
        # pdb.set_trace()
        if serializer.is_valid():
            query = serializer.validated_data
            # pdb.set_trace()
            serializer.save()
            # pdb.set_trace()
            return self.send_response(1, {'phonenumber': query['phonenumber']})
        print serializer.errors
        # pdb.set_trace()
        return self.send_response(0, {'error': serializer.errors})

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return self.send_response(1, {'data': "Successfully deleted"})



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
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            print 'validity check'
            return self.send_response(0, {'error': serializer.errors})
        else:
            print 'else validity check'
            query = serializer.validated_data
            user = AuthUser()
            user.username = query['username']
            user.first_name = query['first_name']
            user.last_name = query['last_name']
            user.email = query['email']
            user.usertype = query['usertype']
            user.phonenumber = query['phonenumber']
            user.set_password(query['password'])
            user.save()
            if self.auth_login({'username': query['username'], 'password': query['password']}):
                print 'login check'
                authuser = AuthUser.objects.get(username=query['username'])
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

    def get_fb_user_data(self, access_token):
        url = "https://graph.facebook.com/v2.5/me?access_token={}&fields=id,first_name,last_name,name,email".format(
            access_token)
        res = requests.get(url)
        print "FACEBOOK DATA : ",res.json()
        return res.json()

    def post(self, request, format=None):
        print request.data
        if request.user.is_authenticated():
            print 'logout'
            logout(request)
            pass
        if request.data['logintype'] == "email":
            serializer = LoginUserSerializer(data=request.data)
            if not serializer.is_valid():
                print 'validity check'
                return self.send_response(0, {'error':"There is an error it seems!"})
            else:
                query = serializer.validated_data
                print 'else validity check'
                if self.auth_login({'username': query['username'], 'password': query['password']}):
                    user = AuthUser.objects.get(username=query['username'])
                    print 'login check'
                    return self.send_response(1, {'session_id':get_session_id(request), 'completed':True, 'id':user.id,'usertype':user.usertype})
                else:
                    return self.send_response(0, {'error':"There is an error it seems!"})

        else:
            req = FbUserSlzr(data=request.data)
            if not req.is_valid():
                return self.send_response(0, {'error':"There is an error it seems!"})
            try:
                user = AuthUser.objects.get(fb_id=request.data['fb_id'])
                if self.auth_login({'fb_id': request.data['fb_id']}):
                    completed = False
                    if user.phonenumber:
                        completed = True
                        pass
                    return self.send_response(1, {'session_id':get_session_id(request), 'completed':completed, 'id':user.id,'usertype':user.usertype})               
            except AuthUser.DoesNotExist:
                user = AuthUser()
                user.username = request.data['username']
                user.fb_id = request.data['fb_id']
                user.usertype = "user"
                user.save() 
                authuser = AuthUser.objects.get(fb_id=request.data['fb_id'])
                if self.auth_login({'fb_id': request.data['fb_id']}):
                    return self.send_response(1, {'session_id': get_session_id(request), 'completed':False, 'id':authuser.id,'usertype':authuser.usertype})               
        return self.send_response(0, {'error':"There is an error it seems!"})





# class GetUserview(CustomView):
#     def get(self, request, pk, format=None):
#         user = AuthUser.objects.get(id=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)