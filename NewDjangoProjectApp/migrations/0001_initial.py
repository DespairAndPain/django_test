# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.CharField(blank=True, max_length=120, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]