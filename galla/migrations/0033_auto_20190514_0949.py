# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-14 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galla', '0032_auto_20190513_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Foodl', 'Food'), ('Fashion', 'Fashion'), ('Weight loss', 'Weight loss')], max_length=120),
        ),
    ]