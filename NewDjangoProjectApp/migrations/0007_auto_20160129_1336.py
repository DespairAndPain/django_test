# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewDjangoProjectApp', '0006_auto_20160129_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task',
            field=models.TextField(blank=True, null=True),
        ),
    ]
