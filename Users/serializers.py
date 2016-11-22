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