# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20171030_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
