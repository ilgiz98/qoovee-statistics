# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 11:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_department_report_statistic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 16, 11, 11, 19, 397132, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='report',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 16, 11, 11, 19, 397238, tzinfo=utc)),
        ),
    ]
