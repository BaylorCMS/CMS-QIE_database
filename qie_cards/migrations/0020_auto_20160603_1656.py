# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qie_cards', '0019_auto_20160603_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attempt',
            old_name='attempt_num',
            new_name='attempt_number',
        ),
        migrations.AddField(
            model_name='attempt',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='passed',
            field=models.BooleanField(default=False),
        ),
    ]
