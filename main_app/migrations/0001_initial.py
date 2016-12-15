# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 21:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Strain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sluf', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=150)),
                ('strength', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='strain_images')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]