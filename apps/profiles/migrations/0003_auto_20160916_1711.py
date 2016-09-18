# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 11:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0002_department_report_statistic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departmant', to='reports.Department'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u0440\u043e\u0444\u0438\u043b\u044c'),
        ),
    ]
