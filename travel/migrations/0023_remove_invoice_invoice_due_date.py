# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-25 00:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luggage', '0022_auto_20161025_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_due_date',
        ),
    ]