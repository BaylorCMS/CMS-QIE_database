# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qie_cards', '0016_auto_20160603_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='abbreviation',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='test',
            name='name',
        ),
    ]
