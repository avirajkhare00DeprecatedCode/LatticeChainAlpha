# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-22 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service1', '0006_newcryptobasket_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcryptobasket',
            name='amount_allocated',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]