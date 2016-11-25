from rest_framework import serializers

from Users.models import *



# class MainUser(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ('id', 'first_name', 'last_name', 'username', 'email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)


class FbUserSlzr(serializers.Serializer):
    fb_id = serializers.CharField(max_length=30)
    username = serializers.CharField(max_length=30)
