# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0006_emailsent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='message',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]