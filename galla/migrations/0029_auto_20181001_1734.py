# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galla', '0028_auto_20181001_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Workout', 'Workout')], max_length=120),
        ),
    ]