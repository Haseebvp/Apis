# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-01 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_auto_20161201_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoptable',
            name='usertype',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
