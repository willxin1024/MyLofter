# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-23 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_auto_20171015_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='gender',
        ),
        migrations.AlterField(
            model_name='comments',
            name='anonymous_user',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='\u533f\u540d'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments',
            field=models.CharField(max_length=100, verbose_name='\u8bc4\u8bba'),
        ),
    ]