from flask import Blueprint,render_template,jsonify,redirect,url_for ,session#url_for:将视图函数转化为url
from exts import mail,db
from flask_mail import Message
from flask import request
import string
import random
from models import EmailCaptchaModel
from .forms import RegisterForm, LoginForm
from models import UserModel
#导入一个可以隐藏密码的库
from werkzeug.security import generate_password_hash,check_password_hash

#访问地址前缀
bp = Blueprint("author",__name__,url_prefix='/author')

@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在！")
                return redirect(url_for("author.login"))
            if check_password_hash(user.password,password):
                """cookie:只能存储内容较少的数据，不适合存储太多的数据,一般用来存储登录授权的东西
                    flask中的session：是经过加密后存储在cookie中的"""
                session['user_id'] = user.id
                return redirect('/')
            else:
                print("密码错误，请重新输入！")
                return redirect(url_for("author.login"))
        else:
            print(form.errors)
            return redirect(url_for("author.login"))

#GET:从服务器上获取数据
#POST：将客户端的数据提交给服务器
@bp.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        #验证用户提交的邮箱和验证码是否对应且正确
        #表单验证：flask-wtf：wtforms一个插件
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form .password.data
            user = UserModel(email=email,username=username,password=generate_password_hash(password))#加密密码赋值给password
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('author.login')) #redirect:表示重新跳转到一个界面
        else:
            print(form.errors)
            return redirect(url_for('author.register'))

#退出登录的视图函数
@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

#bp.route:如果没有指定methods参数，默认就是GET请求
@bp.route('/captcha/email')
def get_email_captcha():
    """两种传参方式：1./captcha/email/<email>
                   2./captcha/email?email=xxx@qq.com"""
    email = request.args.get('email')
    #生成随机几位验证码，可以有数字，字母，数字字母组合
    # string.digits*4:表示从0123456789里面随机取4位数
    source = string.digits * 4
    captcha = random.sample(source,4)
    # print(captcha)
    captcha = ''.join(captcha)
    message = Message(subject='小黑屋注册验证码', recipients=[email], body=f'您的验证码是{captcha}')
    mail.send(message)
    """memcached:缓存数据，存到内存中，适合存储验证码
    redis:存储数据，且有同步功能，即使断电也有保留数据，保存到硬盘中"""
    #用数据库表的方式存储
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTFUL API  返回时格式要求需一致
    return jsonify({'code':200,"message":'','data':None})

@bp.route('/mail/test')
def mail_text():
    message = Message(subject='邮箱测试',recipients=['3306715918@qq.com'],body='这是一条测试邮件')
    mail.send(message)
    return "邮件发送成功"