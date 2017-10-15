from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.

class UserDetails(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):

        return self.user_id.username


class CryptoBasket(models.Model):

    basket_id = models.CharField(max_length=100)
    basket_name = models.CharField(max_length=100)
    basket_info = models.TextField(null=True, blank=True)

    def __unicode__(self):

        return self.basket_name

class UserDefinedBasket(models.Model):

    basket_id = models.CharField(max_length=100)
    basket_name = models.CharField(max_length=100)
    coin_id = models.CharField(max_length=10)

    def __unicode__(self):

        return self.basket_id


class CryptoCoins(models.Model):

    #belongs_to = models.ForeignKey(CryptoBasket, null=True, blank=True)
    coin_name = models.CharField(max_length=100)
    coin_id = models.CharField(max_length=10, null=True, blank=True)
    #allocation_percent = models.CharField(max_length=10, null=True, blank=True)
    ticker_api = models.CharField(max_length=100, null=True, blank=True)
    current_price = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):

        return self.coin_name

class ERC20Tokens(models.Model):

    #belongs_to = models.ForeignKey(CryptoBasket, null=True, blank=True)
    token_name = models.CharField(max_length=100)
    token_id = models.CharField(max_length=100, null=True, blank=True)
    decimals = models.CharField(max_length=50, null=True, blank=True)
    #allocation_percent = models.CharField(max_length=10, null=True, blank=True)
    ticker_api = models.CharField(max_length=100, null=True, blank=True)
    current_price = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):

        return self.token_id

class AllocationObject(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    basket_id = models.CharField(max_length=100)
    coin_id = models.CharField(max_length=100)
    allocation_percent = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):

        return self.coin_id

class TransactionData(models.Model):

    user_id = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    json_data = JSONField(null=True, blank=True)

    def __unicode__(self):

        return self.user_id