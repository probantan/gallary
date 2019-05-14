# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galla', '0003_auto_20180928_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Travel', 'Travel'), ('Fashion', 'Travel'), ('Food', 'Food')], max_length=120),
        ),
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(default='category', max_length=50, verbose_name='Category'),
        ),
    ]