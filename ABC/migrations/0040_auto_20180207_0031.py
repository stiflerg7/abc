# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABC', '0039_event_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('O', 'Ordered'), ('NR', 'Not Ready'), ('R', 'Ready'), ('S', 'Sent'), ('P', 'Paid')], default='Ordered', max_length=50),
        ),
    ]