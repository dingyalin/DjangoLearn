# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('S3', '0002_auto_20161117_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='path',
            name='up_path_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
