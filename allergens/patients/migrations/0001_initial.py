# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('registration_date', models.DateField()),
                ('years', models.IntegerField()),
                ('months', models.IntegerField()),
                ('attending_doctor', models.CharField(max_length=200)),
            ],
        ),
    ]