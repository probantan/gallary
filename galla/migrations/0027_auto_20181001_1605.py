# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galla', '0026_auto_20181001_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(choices=[('NationalPark', 'NationalPark'), ('Gymstore', 'Gymstore'), ('ParadiceLost', 'ParadiceLost'), ('TreebeadsTexas', 'TreebeadsTexas'), ('MombasaCity', 'MombasaCity')], max_length=120),
        ),
    ]
