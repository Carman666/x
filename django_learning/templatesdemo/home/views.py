from django.shortcuts import render,HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "../templates/index.html")

def baidu(request):
    return render(request,"baidu.html")

def info(request):
    #1.普通传参
    username = "小天地小课堂"
    #2.字典类型
    book = {"name":"水浒传","author":"施耐庵"}
    #3.列表
    books = [{"name": "水浒传", "author": "施耐庵"},
             {"name": "三国演义", "author": "罗贯中"}
    ]
    #4.对象
    class Person:
        def __init__(self,realname):
            self.realname = realname
    context = {
        'username': username,
        "book": book,
        "books":books,
        "person":Person('小天地你值得拥有')
    }
    return render(request,"info.html",context=context)

def if_view(request):
    age = 19
    return render(request,"if.html",context={"age":age})

def for_view(request):
    #1.列表
    books = [{"name": "水浒传", "author": "施耐庵"},
             {"name": "三国演义", "author": "罗贯中"}
    ]
    #2.字典
    person = {
        'realname': "小天地",
        "age": 19,
        "height" : 180
    }
    context = {
        'books': books,
        'person': person,
    }
    return render(request,"for.html",context)

def with_view(request):
    context = {
        'books' :[
            {"name": "水浒传", "author": "施耐庵"},
            {"name": "三国演义", "author": "罗贯中"}
    ]}
    return render(request,"with.html",context)

def url_view(request):
    return render(request,"url.html")

def book_detail(request,book_id):
    return HttpResponse(f'您访问的图书id是：{book_id}')

def filter_view(request):
    greet = "Hello World"
    context = {
        'greet': greet,
        'birthday':datetime.now(),
        'profile':"少年借微光成长",
        'html':'<h1>小天地</h1>'
    }
    return render(request,"filter.html",context)

def include_view(request):
    return render(request, '1_base.html')

def static_view(request):
    return render(request,'static.html')