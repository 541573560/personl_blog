# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170912_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author_massage',
            name='name',
            field=models.CharField(max_length=50, verbose_name='姓名'),
        ),
    ]
