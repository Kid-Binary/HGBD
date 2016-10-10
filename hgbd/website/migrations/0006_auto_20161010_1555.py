# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20161010_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='image_list',
            field=models.ImageField(blank=True, null=True, upload_to='service/images/list/', verbose_name='Зображення до списку'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image_main',
            field=models.ImageField(blank=True, null=True, upload_to='service/images/main/', verbose_name='Головне зображення'),
        ),
    ]
