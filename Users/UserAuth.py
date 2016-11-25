import types

from django.contrib.auth.models import User
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.utils import six
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from Users.models import *
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings



class CustomView(APIView):

    def send_response(self, status, data=None):
        if status == 1:
            return Response({'status': 'success', 'data': data})
        if status == 0:
            return Response({'status': 'error', 'data': data or "Sorry, Please try later."})

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(CustomView, self).dispatch(*args, **kwargs)



class FBAuthBackend(object):

    def authenticate(self, fb_id=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = AuthUser.objects.get(fb_id=fb_id)
            return user
        except AuthUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return AuthUser.objects.get(pk=user_id)
        except AuthUser.DoesNotExist:
            return None
