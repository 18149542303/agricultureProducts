#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-11-10 下午4:02
# @Author  : Kirito
# @Site    : 
# @File    : login.py
# @Software: PyCharm
from flask import Blueprint, send_file

login_opt = Blueprint('login', __name__)

@login_opt.route('/')
def index():
    return send_file('templates/index.html')

@login_opt.route('/login')
def login():
    return send_file('templates/login.html')

@login_opt.route('/register')
def register():
    return send_file('templates/register.html')

@login_opt.route('/test')
def test():
    return send_file('templates/test.html')
