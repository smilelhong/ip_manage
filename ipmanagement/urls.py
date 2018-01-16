# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from django.conf.urls import patterns,url
from ipmanagement.views import Index,Ip_range

urlpatterns = patterns(
    'ipmanagement.views',
    url(r'^$', Index.as_view(),name='index'),
    url(r'^ip_range_list/$', Ip_range.as_view()),
    url(r'^ip_range_add/$', Ip_range.as_view(),name='ip_range_add'),
    url(r'^all-ip/$', 'all_ip_list'),
    url(r'^use-ip/$', 'ip_use_list'),
    url(r'^unuse-ip/$', 'ip_unuse_list'),
)
