#接收邮箱and 加密,用于写所有要用到的配置

#加密的字符串
SECRET_KEY = 'sjhfusajfbsdufhksdg'

#数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'answer'
USERNAME = 'root'
PASSWORD = '507680'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

#邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '3125115019@qq.com'
MAIL_PASSWORD = 'rnpwigeovuhideaj'
MAIL_DEFAULT_SENDER = '3125115019@qq.com'
