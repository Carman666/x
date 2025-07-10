from django.shortcuts import render

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