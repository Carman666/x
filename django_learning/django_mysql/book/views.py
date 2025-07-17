from django.shortcuts import render,HttpResponse
#导入sql数据库文件信息
from django.db import connection

# Create your views here.
def index(request):
    #获取游标对象
    cursor = connection.cursor()
    #拿到游标对象后执行sql语句
    cursor.execute('select * from book')
    #获取所有数据
    rows = cursor.fetchall()
    #遍历查询到的数据
    for row in rows:
        print(row)
    return HttpResponse("查找成功")