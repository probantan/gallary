# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Travel', 'Travel'), ('Fashion', 'Travel'), ('Food', 'Food')], max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='gallary/')),
                ('Image_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50, verbose_name='category')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('Nation Park', 'Nation Park'), ('Bonfire Adventures', 'Bonfire Adventures'), ('Paradice Lost', 'Paradice Lost'), ('Hardstone-Ottawa', 'Hardstone-Ottawa'), ('Treebeads-Texas', 'Treebeads-Texas'), ('Mombasa-City', 'Mombasa-City')], max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='galla.Location'),
        ),
    ]