# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-05 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserver', '0008_cruise_number_of_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='identity_document_types',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='identity_document_types',
        ),
    ]
