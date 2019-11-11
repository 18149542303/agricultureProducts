#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-11-10 下午4:03
# @Author  : Kirito
# @Site    : 
# @File    : order.py
# @Software: PyCharm
from flask import Blueprint, send_file

order_opt = Blueprint('order', __name__)

@order_opt.route('/test')
def test():
    return send_file('templates/test.html')

