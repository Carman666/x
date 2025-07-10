from flask import Flask,session,g #g：用于存储全局变量
import config
from exts import db,mail
from models import UserModel
from blueprint.author import bp as author_bp
from blueprint.ask_question import bp as ask_question_bp
from flask_migrate import Migrate

app = Flask(__name__)
#清除模板缓存
app.jinja_env.cache = {}
#绑定配置文件
app.config.from_object(config)
#先创建app,后绑定app
db.init_app(app)
#导入mail的app
mail.init_app(app)

migrate = Migrate(app,db)
#注册蓝图
app.register_blueprint(author_bp)
app.register_blueprint(ask_question_bp)


#before_requset/before_first_request/after_request
#钩子函数（hook）：在其他代码在运行过程中，突然穿插进来执行
@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        user= UserModel.query.get(user_id)
        setattr(g,'user',user)
    else:
        setattr(g,'user',None)

@app.context_processor
def my_context_processor():
    return {'user': g.user}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
