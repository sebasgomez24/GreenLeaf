# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strain',
            name='strength',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1),
        ),
    ]
