# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0002_auto_20170627_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=250),
        ),
    ]
