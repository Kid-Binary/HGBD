# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-16 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0002_auto_20161012_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metadata',
            options={'verbose_name': 'Метадані', 'verbose_name_plural': 'Метадані'},
        ),
    ]
