#从flask这个包里导入flask类,request全局对象
from flask import Flask,request

#使用flask类创建一个app对象
#__name__:嗲表当前app.py这个模块
"""以后出现bug，可以帮我们快速定位
对于寻找模板文件，有一个相对路径"""
app = Flask(__name__)

#创建一个路由和视图函数的映射
#“/”表示根路由
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/myself')
def myself():
    return "这是个人中心"

@app.route('/blog/list')
def blog_list():
    return "我是博客列表"

#带参数的url：将带参数固定到path中
@app.route('/blog/<int:blog_id>')  #int定义id类型
def blog(blog_id):
    return "你访问的博客时：%s" % blog_id

#查询字符串的方式传参
@app.route('/book/list')
def book_list():
    #args：参数  request.args:类字典类型
    page = request.args.get("page",default=1,type=int)
    return f"你获取的是第{page}页的图书列表"

if __name__ == '__main__':
    app.run()
