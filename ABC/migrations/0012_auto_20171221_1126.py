# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABC', '0011_auto_20171221_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='cif',
            field=models.CharField(max_length=25),
        ),
    ]
