# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-11 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryWay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField(help_text='\u5355\u4f4d\u662f\u4fbf\u58eb')),
                ('logo', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('show', models.BooleanField(default=1)),
                ('type2', models.CharField(default=b'self', max_length=5)),
            ],
        ),
    ]