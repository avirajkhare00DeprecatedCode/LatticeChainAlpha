# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_end', '0006_tradablesets_is_filled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradablesets',
            name='basket_address',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
