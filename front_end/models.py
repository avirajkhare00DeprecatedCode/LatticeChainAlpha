from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ERC20Address(models.Model):

    user_id = models.ForeignKey(User)
    token_address = models.CharField(max_length=100)
    network_id = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):

        return self.token_address