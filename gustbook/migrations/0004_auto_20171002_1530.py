# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gustbook', '0003_words_board_e_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words_board',
            name='e_mail',
            field=models.EmailField(max_length=254),
        ),
    ]
