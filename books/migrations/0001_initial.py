# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=40)),
                ('publication_date', models.DateField()),
            ],
        ),
    ]
