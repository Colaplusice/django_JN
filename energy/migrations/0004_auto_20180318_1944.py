# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0003_auto_20180318_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.Type'),
        ),
    ]
