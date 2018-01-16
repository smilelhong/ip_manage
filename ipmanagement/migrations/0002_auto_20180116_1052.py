# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ipmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IP_Range',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_ip', models.GenericIPAddressField(verbose_name='\u5f00\u59cbIP')),
                ('end_ip', models.GenericIPAddressField(verbose_name='\u7ed3\u675fIP')),
                ('network', models.GenericIPAddressField(verbose_name='\u7f51\u7edc\u53f7')),
                ('netmask', models.CharField(default=b'', max_length=20, verbose_name='\u63a9\u7801')),
                ('use_ip', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u5df2\u4f7f\u7528IP\u6570', blank=b'')),
                ('left_ip', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u672a\u4f7f\u7528IP\u6570', blank=b'')),
                ('create_time', models.DateField(default=datetime.datetime(2018, 1, 16, 10, 52, 6, 830000), verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
        migrations.AlterField(
            model_name='ip_address',
            name='apply_time',
            field=models.DateField(default=datetime.datetime(2018, 1, 16, 10, 52, 6, 828000), verbose_name='\u7533\u8bf7\u65f6\u95f4'),
        ),
    ]
