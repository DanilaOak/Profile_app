# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0004_auto_20170719_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilechange',
            name='change_date',
            field=models.DateTimeField(),
        ),
    ]
