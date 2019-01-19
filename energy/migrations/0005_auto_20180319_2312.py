# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("energy", "0004_auto_20180318_1944")]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="type",
            field=models.ForeignKey(
                db_column="name",
                on_delete=django.db.models.deletion.CASCADE,
                to="energy.Type",
            ),
        ),
        migrations.AlterField(
            model_name="type",
            name="name",
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
