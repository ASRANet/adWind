# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=30)),
                ('headline', models.CharField(max_length=40)),
                ('element_id', models.CharField(max_length=40, unique=True)),
                ('order', models.IntegerField(unique=True)),
                ('type', models.CharField(max_length=10)),
                ('text', models.CharField(max_length=2000)),
            ],
        ),
    ]