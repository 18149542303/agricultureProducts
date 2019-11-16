# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-16 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_trade_name', models.CharField(max_length=20, verbose_name='商品名称')),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格')),
                ('goods_spec', models.CharField(max_length=20, verbose_name='规格')),
                ('goods_simple_explain', models.CharField(blank=True, max_length=50, verbose_name='商品简介')),
                ('goods_details', models.CharField(blank=True, max_length=500, verbose_name='商品详情')),
                ('goods_stock', models.CharField(max_length=30, verbose_name='库存')),
                ('goods_picture', models.ImageField(blank=True, upload_to='static/goods_images', verbose_name='商品图片')),
                ('goods_create_datatime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('goods_update_datatime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('goods_is_active', models.BooleanField(default=True, verbose_name='存活')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'goods',
            },
        ),
    ]
