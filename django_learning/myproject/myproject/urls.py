"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,reverse
from django.shortcuts import HttpResponse
from book import views

#URL与视图的映射
"""/s(URL) -> 视图函数，进行映射"""

def index(request):
    reverse("book_detail_query_string")
    #普遍的url反转
    """print(reverse("book_detail_query_string"))"""
    #传递带有参数的反转
    """print(reverse("book_   ",kwargs={"id":1},))"""
    #添加带有查询字符串的反转，需要手动添加eg./book?id=1
    """print(reverse("book_detail_query_string" + "?id=1")"""
    #将带有指定命名空间的视图函数进行反转
    """print(reverse(movie:movie_list))"""
    return HttpResponse("欢迎来到门的世界！")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name="index"),
    path('book',views.book_detail_query_string,name='book_detail_query_string'),#string后面跟着的括号删除
    #如果添加了int，限制类型，且表示在浏览器中，book_id只能出现整形，出现非整形时会出现404报错
    path('book/<book_id>',views.book_detail_path),
#导入movie中的path模块
    path("movie/",include("movie.urls"))
]
