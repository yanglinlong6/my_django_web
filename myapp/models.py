from django.db import models
import django.utils.timezone as timezone


# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=512, blank=True)
    age = models.CharField(max_length=512)

    class Meta:
        db_table = 't_user'
        # ordering = ['-date_time']


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='书籍名称')
    price = models.FloatField(verbose_name='书籍价格')
    pub_date = models.DateField(verbose_name='出版日期')
    publish = models.CharField(max_length=32, verbose_name='出版社名称')

    # 当打印book对象时，通过 __str__ 的返回更友好的结果
    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_book'
        verbose_name = '书籍数据'


class Order(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, verbose_name="订单ID", help_text="订单ID")
    order_title = models.CharField(verbose_name='订单名字', max_length=255, null=True)
    order_content = models.CharField(verbose_name='工单内容', max_length=255, null=True)
    status = models.IntegerField(verbose_name='工单状态', default=0)
    created_by = models.IntegerField(verbose_name='创建人')
    created_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated_by = models.IntegerField(verbose_name='更新人', null=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', null=True)

    # 当打印book对象时，通过 __str__ 的返回更友好的结果
    def __str__(self):
        return self.order_title

    class Meta:
        db_table = 't_order'
        verbose_name = '订单表'
