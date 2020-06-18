import os
DEBUG = True

SECRET_KEY = os.urandom(24)
HOSTNAME = '127.0.0.1'
PORT = '5432'
DATABASE = 'flaskdb'
USERNAME = 'postgres'
PASSWORD = '123456'
DB_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'\
    .format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI  # 连接数据库
SQLALCHEMY_TRACK_MODIFICATIONS = True  # 跟踪数据库变化，会影响代码效率
# SQLALCHEMY_ECHO = True  # 展示sql语句
# SQLALCHEMY_POOL_SIZE = 5  # 连接池大小
# SQLALCHEMY_POOL_TIMEOUT = 15  # 配置超时时间
