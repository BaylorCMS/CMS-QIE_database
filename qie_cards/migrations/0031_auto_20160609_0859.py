# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qie_cards', '0030_auto_20160609_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qiecard',
            name='uid',
            field=models.CharField(default='', max_length=18, unique=True),
        ),
    ]
