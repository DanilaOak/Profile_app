# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_profilechange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilechange',
            name='change_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
