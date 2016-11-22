from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AuthUser(User):
	# user = models.OneToOneField(User)
	usertype = models.CharField(max_length=50)
	phonenumber = models.CharField(max_length=10)

	def __unicode__(self):
		return unicode(self.username)