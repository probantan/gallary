# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galla', '0016_auto_20180930_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(choices=[('National Park', 'National Park'), ('Gym-store', 'Gym-store'), ('Paradice Lost', 'Paradice Lost'), ('Treebeads-Texas', 'Treebeads-Texas'), ('Mombasa-City', 'Mombasa-City')], max_length=120),
        ),
    ]
