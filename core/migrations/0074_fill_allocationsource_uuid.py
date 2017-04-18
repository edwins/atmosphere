# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-29 18:34
from __future__ import unicode_literals

from django.db import migrations, models

import uuid

def uuid_for_allocationsource(apps,schema_editor):
    CoreModel = apps.get_model('core','AllocationSource')
    attr = 'uuid'
    for row in CoreModel.objects.all():
        if hasattr(row,attr) and not getattr(row,attr):
            new_uuid = str(uuid.uuid4())
            setattr(row,attr,new_uuid)
            row.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_allocationsource_uuid'),
    ]

    operations = [
        migrations.RunPython(
            uuid_for_allocationsource,
            reverse_code=migrations.RunPython.noop),
    ]