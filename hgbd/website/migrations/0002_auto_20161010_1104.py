# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 08:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicelistitem',
            old_name='text_uk',
            new_name='text',
        ),
    ]