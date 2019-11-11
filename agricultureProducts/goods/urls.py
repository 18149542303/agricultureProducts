#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-11-10 下午3:45
# @Author  : Kirito
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'', views.test_view)
]
