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


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # name = db.Column(db.String(32))
    title = db.Column(db.String(64), unique=True)
    content = db.Column(db.Text)


# art1 = Article(id=1, title='first', content='this is first test')
# art2 = Article(id=2, title='second', content='this is second test')
# art3 = Article(id=3, title='sovereign', content='this is sovereign test')
# db.session.add_all([art1, art2, art3])
# db.session.commit()

# art4 = Article(id=5, title='five', content='tsitsa five sst')
# db.session.add(art4)
# db.session.commit()


if __name__ == '__main__':
    manager.run()
