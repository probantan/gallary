# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galla', '0027_auto_20181001_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(choices=[('National Park', 'National Park'), ('Gyms-tore', 'Gym-store'), ('Paradice Lost', 'Paradice Lost'), ('Treebeads Texas', 'Treebeads-Texas'), ('Mombasa City', 'Mombasa-City')], max_length=120),
        ),
    ]
