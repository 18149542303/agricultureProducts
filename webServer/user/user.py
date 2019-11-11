#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-11-10 下午4:02
# @Author  : Kirito
# @Site    : 
# @File    : user.py
# @Software: PyCharm
from flask import Blueprint, send_file

user_opt = Blueprint('user', __name__)

@user_opt.route('/<username>/info')
def info(username):
    # 个人信息
    return send_file('templates/user/about.html')


@user_opt.route('/<username>/change_info')
def change_info(username):
    # 修改个人信息
    return send_file('templates/user/change_info.html')
