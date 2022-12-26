#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/9/16 9:25
# @Author : caozhi1214@qq.com
# @File : urls.py
# @Software: PyCharm
# Description:


from django.urls import path

from .views import CveOriginUpstreamView

urlpatterns = [

    # http://{{host}}/api/v1/component-report
    path(r'v1/component-report', CveOriginUpstreamView.as_view(), name='cve_origin_upstream'),  # 获取cve_id

]
