from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserExtendDetails(models.Model):

    userid = models.OneToOneField(User)
    full_name = models.CharField(max_length=40, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    bitcoin_private_key = models.CharField(max_length=100, null=True, blank=True)
    bitcoin_public_key = models.CharField(max_length=100, null=True, blank=True)
    neo_public_key = models.CharField(max_length=100, null=True, blank=True)
    neo_private_key = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):

        return self.userid.username