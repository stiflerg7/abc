# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-19 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABC', '0014_auto_20180119_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]