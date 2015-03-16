# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=64, verbose_name=b'\xe5\x9b\xbe\xe6\x96\x87\xe6\xa0\x87\xe9\xa2\x98')),
                ('Description', models.CharField(max_length=120, null=True, verbose_name=b'\xe5\x9b\xbe\xe6\x96\x87\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('PicUrl', models.URLField(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe9\x93\xbe\xe6\x8e\xa5')),
                ('Url', models.URLField(verbose_name=b'\xe7\xbd\x91\xe9\xa1\xb5\xe9\x93\xbe\xe6\x8e\xa5')),
                ('Chuangjianshijian', models.DateField(verbose_name=b'\xe5\x9b\xbe\xe6\x96\x87\xe6\xb6\x88\xe6\x81\xaf\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-Chuangjianshijian'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FromUserName', models.CharField(max_length=30, verbose_name=b'\xe5\x8f\x91\xe5\x87\xba\xe6\xb6\x88\xe6\x81\xaf\xe8\x80\x85')),
                ('CreateTime', models.CharField(max_length=15, verbose_name=b'\xe6\xb6\x88\xe6\x81\xaf\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('zhuangtai', models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('zhuangtai_ma', models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81\xe7\xa0\x81', blank=True)),
                ('zhuangtai_time', models.CharField(max_length=15, null=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe7\x8a\xb6\xe6\x80\x81\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
