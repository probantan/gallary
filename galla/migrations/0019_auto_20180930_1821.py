# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galla', '0018_auto_20180930_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='Category',
            new_name='category',
        ),
    ]