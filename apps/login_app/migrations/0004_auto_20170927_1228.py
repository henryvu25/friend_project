# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.IntegerField(),
        ),
    ]
