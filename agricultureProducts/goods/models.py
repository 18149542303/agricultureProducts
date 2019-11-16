from django.db import models

# Create your models here.

class Goods(models.Model):
    goods_trade_name = models.CharField(max_length=20,verbose_name='商品名称')
    goods_price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='商品价格')
    goods_spec = models.CharField(max_length=20,verbose_name='规格')
    goods_simple_explain = models.CharField(max_length=50,verbose_name='商品简介',blank=True)
    goods_details = models.CharField(max_length=500,verbose_name='商品详情',blank=True)
    goods_stock = models.CharField(max_length=30,verbose_name='库存')
    goods_picture = models.ImageField(upload_to='media/img/goods_images',verbose_name='商品图片',blank=True)
    goods_create_datatime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    goods_update_datatime = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    goods_is_active = models.BooleanField(verbose_name='存活',default=True)

    def __str__(self):
        return '{}'.format(self.goods_trade_name,self.goods_price,self.goods_spec,self.goods_simple_explain,self.goods_details,self.goods_stock)
        

    class Meta:
        db_table = 'goods'
        verbose_name ='商品'
        verbose_name_plural = verbose_name










