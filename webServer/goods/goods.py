#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-11-10 下午4:02
# @Author  : Kirito
# @Site    : 
# @File    : goods.py
# @Software: PyCharm
from flask import Blueprint, send_file

goods_opt = Blueprint('goods', __name__)

@goods_opt.route('/test')
def test():
    return send_file('templates/test.html')

