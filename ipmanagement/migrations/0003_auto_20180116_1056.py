# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ipmanagement', '0002_auto_20180116_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip_range',
            name='des',
            field=models.CharField(default=b'', max_length=20, null=True, verbose_name='\u63cf\u8ff0', blank=b''),
        ),
        migrations.AlterField(
            model_name='ip_address',
            name='apply_time',
            field=models.DateField(default=datetime.datetime(2018, 1, 16, 10, 56, 54, 173000), verbose_name='\u7533\u8bf7\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='ip_range',
            name='create_time',
            field=models.DateField(default=datetime.datetime(2018, 1, 16, 10, 56, 54, 175000), verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]
