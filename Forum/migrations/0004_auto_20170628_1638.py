# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 16:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0003_auto_20170627_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='user',
        ),
        migrations.DeleteModel(
            name='User_details',
        ),
    ]
