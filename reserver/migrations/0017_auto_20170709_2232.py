# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-09 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserver', '0016_auto_20170707_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cruise',
            options={},
        ),
        migrations.RemoveField(
            model_name='cruise',
            name='start_date',
        ),
    ]
