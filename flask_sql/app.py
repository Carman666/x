from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#mysql所在的主机名
HOSTNAME = '127.0.0.1'
#mysql监听的端口号
PORT = 3306
#连接MySQL的用户名，读者用自己设置的
USERNAME = 'root'
#用户密码，自己设置
PASSWORD = '507680'
#MySQL上创建的数据库的名字
DATABASE = 'database_learn'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'

#在app.config中设置好连接数据库的信息
#然后连接SQLAlchemy（app）创建的db对象
#SQLAlchemy会自动读取app.config中连接数据库的信息
db = SQLAlchemy(app)
#用此来映射到数据库
migrate = Migrate(app, db)

"""ORM模型映射成表三部曲
1.flask db init:这部只需执行一次
如果修改了数据库中表的内容，只需执行后两部，前一部不用执行
2.flask db migrate:识别ORM模型的改变，生成迁移脚本
3.flask db upgrade:运行迁移脚本，同步到数据库中"""

#用于测试数据库是否连接成功
# with app.app_context():   #请求上下文
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 1"))
#         print(rs.fetchone()) #如果输出（1，）则连接成功

#orm模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    signature = db.Column(db.String(200),nullable=False)

    # 下面运用要与上面一一对应，但是比较麻烦，另一种更快更简易，但是不明显
    # articles = db.relationship('Article', back_populates="author")

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text,nullable=False)

    #添加作者的外键
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    # author = db.relationship("user",back_populates='articles')  #back_populates反向引用
    """backref:自动给user模型添加一个articles的属性，用来获取文章列表"""
    author = db.relationship("User", backref='articles')


# article.author_id = user.id
# user = User.query.get(article.author_id)
# article.author = User.quety.get(article.author_id)
# print(article.author)


# with app.app_context():
    #先删除所有表
    # db.drop_all()
    #再重新创建表
    # db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/user/add')
def add_user():
    #创建ORM对象
    user = User(username = "Carmen", password = "123456")
    #将ORM对象添加到db.session
    db.session.add(user)
    #将db.session中的改变同步到数据库中
    db.session.commit()
    return "用户创建成功！"

@app.route('/user/query')
def query_user():
    """get查找，根据主键查找"""
    # user = User.query.get(1)
    # print(f"{user.id}:{user.username}->{user.password}")
    """filter_by查找  Query：类数组"""
    users = User.query.filter_by(username = "Carmen")
    for user in users:
        print(user.username)
    return "数据查找成功"

@app.route('/user/update')
def update_user():
    user = User.query.filter_by(username = "Carmen").first()
    user.password = '258369'
    db.session.commit()
    return "数据修改成功"

@app.route('/user/delete')
def delete_user():
    #查找
    user = User.query.get(1)
    #从db.session中删除
    db.session.delete(user)
    #将db.session中的修改，同步到数据库中
    db.session.commit()
    return "数据删除成功"

@app.route('/article/add')
def article_add():
    article1 = Article(title="Flask学习大纲", content='Flask哈哈哈哈')
    article1.author = User.query.get(2)

    article2 = Article(title="Django学习大纲", content='Django哦哦哦哦哦')
    article2.author = User.query.get(2)
    db.session.add_all([article1, article2])
    db.session.commit()
    return "文章添加成功"

@app.route('/article/query')
def article_query():
    user = User.query.get(2)
    for article in user.articles:
        print(article.title)
    return "文章查找成功"



if __name__ == '__main__':
    app.run()
