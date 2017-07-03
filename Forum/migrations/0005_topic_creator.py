# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 16:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Forum', '0004_auto_20170628_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]