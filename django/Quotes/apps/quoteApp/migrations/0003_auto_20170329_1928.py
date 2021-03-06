# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quoteApp', '0002_auto_20170329_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='author',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subuser', to='lrApp.User'),
        ),
    ]
