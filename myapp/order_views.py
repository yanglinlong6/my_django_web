# Create your views here.
import datetime
import json
import logging

from django.http import HttpResponse
from . import models
from datetime import date, datetime


def save_order(request):
    postbody = request.body
    json_param = json.loads(postbody.decode())
    order_title = json_param.get('order_title')
    order_content = json_param.get('order_content')
    status = json_param.get('status')
    print(status, order_title, order_content)
    models.Order(
        order_title=order_title,
        order_content=order_content,
        status=status,
        created_by=1
    ).save()
    return HttpResponse("ok")


def getOrderList(request):
    objects_all = models.Order.objects.all()
    print(objects_all)
    return HttpResponse("list" + json.dumps(list(objects_all.values()), cls=ComplexEncoder))


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
