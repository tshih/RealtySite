# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 05:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_Name', models.CharField(max_length=200)),
                ('page_Description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='WebTextField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_Field_Name', models.CharField(default='index', max_length=200)),
                ('question_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('web_Page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srFrontend.WebPage')),
            ],
        ),
    ]
