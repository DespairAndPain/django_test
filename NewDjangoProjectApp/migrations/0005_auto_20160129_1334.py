# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewDjangoProjectApp', '0004_auto_20160129_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]