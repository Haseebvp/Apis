# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-01 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_shoptable_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoptable',
            name='gcm_token',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
