# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20160928_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='introcontent',
            name='headline_uk',
        ),
        migrations.AddField(
            model_name='introcontent',
            name='headline_in_uk',
            field=models.CharField(default='-', max_length=50, verbose_name='Слоган (вступ)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='introcontent',
            name='headline_out_uk',
            field=models.CharField(default='-', max_length=50, verbose_name='Слоган (висновок)'),
            preserve_default=False,
        ),
    ]