from django.db import models


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
