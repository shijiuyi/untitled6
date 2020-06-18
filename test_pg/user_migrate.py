from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager  # 用命令操作的扩展包
from flask_migrate import Migrate, MigrateCommand  # 操作数据库迁移文件的扩展包


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://' \
                                        'postgres:123456@localhost/test_migrate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 显示数据库操作的原生数据就是直接在数据库操作的数据，便于查错
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
manager = Manager(app)
# 创建迁移对象
migrate = Migrate(app, db)
# 将迁移文件的命令添加到‘db’中
manager.add_command('db', MigrateCommand)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), unique=True)
    info = db.Column(db.String(128))
    users = db.relationship("Users", backref='role')


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    info = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


@app.route('/')
def hello():
    return 'hello flask migrate'


if __name__ == '__main__':
    manager.run()

"""
比如上面的代码所在的文件名称为database.py。
1.python database.py db init 　生成管理迁移文件的migrations目录
2.python database.py db migrate -m "注释"　　 在migrations/versions中生成一个文件，该文件记录数据表的创建和更新的不同版本的代码。
3.python database.py db upgrade　　在数据库中生成对应的表格。
4.当需要改表格的时候，改完先执行第二步，然后再执行第三步。
5.需要修改数据表的版本号的时候需要做的操作如下：
python database.py db upgrade 版本号　　向上修改版本号
python database.py db downgrade 版本号 　　向下修改版本号
可能用到的其他的语句：
python database.py db history 　　查看历史版本号
python database.py db current 　　查看当前版本号
"""
