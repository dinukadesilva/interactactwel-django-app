# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-26 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subbasin',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('detail_json', jsonfield.fields.JSONField()),
            ],
            options={
                'verbose_name': 'Subbasin',
                'verbose_name_plural': 'Subbasins',
                'db_table': 'subbasin',
                'managed': True,
            },
        ),
    ]
