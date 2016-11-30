# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-30 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Location', '0001_initial'),
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoptable',
            old_name='name',
            new_name='shop',
        ),
        migrations.AddField(
            model_name='shoptable',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shoptable',
            name='details',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='shoptable',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Location.LocationTable'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoptable',
            name='shop_type',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
