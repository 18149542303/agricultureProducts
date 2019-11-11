# -*- coding:utf-8 -*-
######################################################
#     > File Name: flask_client.py
#     > Author: GuoXiaoNao
#     > Mail: 250919354@qq.com
#     > Created Time: Mon 20 May 2019 11:52:00 AM CST
######################################################

from flask import Flask, request, send_file

from login.login import login_opt
from goods.goods import goods_opt
from user.user import user_opt
from order.order import order_opt

app = Flask(__name__)


# IP拦截
# @app.before_request
# def before_request():
#     ip = request.remote_addr
#     ips = ['176.136.4.6', '127.0.0.1']
#     if ip not in ips:
#         print('有未知人请求', ip)
#         return send_file('templates/forbidden.html')


app.register_blueprint(goods_opt, url_prefix='/goods')
app.register_blueprint(user_opt, url_prefix='/user')
app.register_blueprint(order_opt, url_prefix='/order')
app.register_blueprint(login_opt, url_prefix='')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

