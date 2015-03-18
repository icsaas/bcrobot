# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30, verbose_name='\u8ba2\u9605\u8005')),
                ('channel', models.CharField(max_length=30, verbose_name='\u8ba2\u9605\u901a\u9053')),
                ('url', models.CharField(max_length=100, verbose_name='webhook\u5730\u5740')),
                ('token', models.CharField(max_length=100, verbose_name='Token')),
                ('spacename', models.CharField(max_length=30, verbose_name='\u7a7a\u95f4\u540d')),
                ('subtype', models.CharField(max_length=30, verbose_name='\u8ba2\u9605\u7c7b\u578b')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
