# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0002_auto_20170711_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_ip', models.CharField(max_length=20)),
                ('change_date', models.DateTimeField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.Profile')),
            ],
        ),
    ]
