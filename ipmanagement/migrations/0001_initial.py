# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IP_Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(verbose_name='IP\u5730\u5740')),
                ('gateway', models.GenericIPAddressField(verbose_name='\u7f51\u5173')),
                ('network', models.GenericIPAddressField(verbose_name='\u7f51\u7edc\u53f7')),
                ('netmask', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u63a9\u7801', blank=b'')),
                ('system', models.CharField(default=b'', max_length=64, null=True, verbose_name='\u5e94\u7528\u7cfb\u7edf', blank=b'')),
                ('apply_person', models.CharField(default=b'', max_length=64, null=True, verbose_name='\u7533\u8bf7\u4eba', blank=b'')),
                ('state', models.CharField(max_length=20, verbose_name='\u72b6\u6001', choices=[('\u5df2\u5206\u914d', '\u5df2\u5206\u914d'), ('\u672a\u5206\u914d', '\u672a\u5206\u914d')])),
                ('apply_time', models.DateField(default=datetime.datetime(2018, 1, 16, 10, 27, 23, 994000), verbose_name='\u7533\u8bf7\u65f6\u95f4')),
            ],
        ),
    ]
