from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

USER_TYPES = (
    ('shop', ['shop']),
    ('user', ['user']),
    )


class AuthUser(User):
	# user = models.OneToOneField(User)
	usertype = models.CharField(max_length=50, choices=USER_TYPES)
	phonenumber = models.CharField(max_length=10, null=True)
	fb_id = models.CharField(max_length=100, null=True, blank=True)
	gcm_token = models.CharField(max_length=1000, null=True, blank=True)

	def __unicode__(self):
		return unicode(self.username)
