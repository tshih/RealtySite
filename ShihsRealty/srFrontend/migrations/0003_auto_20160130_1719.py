# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srFrontend', '0002_auto_20160126_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webtextfield',
            name='web_Page',
        ),
        migrations.AddField(
            model_name='webtextfield',
            name='web_Page',
            field=models.ManyToManyField(to='srFrontend.WebPage'),
        ),
    ]
