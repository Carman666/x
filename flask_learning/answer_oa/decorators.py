#添加装饰器
from functools import wraps
from flask import g,redirect,url_for

def login_required(func):
    #保留func信息
    @wraps(func)
    def inner(*args, **kwargs):  #两个表示万能参数，*args：表示位置参数
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('author.login'))
    return inner

# @login_required
# def public_question(func):
#     pass
#
# login_required(public_question)(question_id)