# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qie_cards', '0023_tester_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='description',
            field=models.TextField(default='', max_length=1500),
        ),
    ]
