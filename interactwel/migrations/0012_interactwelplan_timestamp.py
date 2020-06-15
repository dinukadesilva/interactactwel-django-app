# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-02 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interactwel', '0011_interactwelplan_actions'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactwelplan',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
