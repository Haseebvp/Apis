# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-23 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20161118_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='phonenumber',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
