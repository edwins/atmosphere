# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0094_instancestatushistory_add_jsonfield_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootscript',
            name='wait_for_deploy',
            field=models.BooleanField(default=True),
        ),
    ]
