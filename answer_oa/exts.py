#这个文件用于解决循环应用的问题
#用于编写第三方插件
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()