from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . import models


def query():
    # 添加数据 方式1
    book_obj = models.Book(
        # 对于主键 id 可以不传值，默认即可
        title='红楼梦',
        price=9.9,
        # 添加时间日期类型的数据时可以是日期时间类型的对象，也可以是字符串
        # pub_date=datetime.datetime.now(),
        pub_date='2020-1-5',
        publish='机械工业出版社'
        # 对于有默认值或者为空的字段，视具体情况而定
    )
    book_obj.save()

def index(request):
    query()
    print("=====")
    objects_all = models.User.objects.all()
    print(objects_all)
    return HttpResponse("Hello, world. You're at the polls index.")
