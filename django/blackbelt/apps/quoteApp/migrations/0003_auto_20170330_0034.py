# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteApp', '0002_favorite_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
