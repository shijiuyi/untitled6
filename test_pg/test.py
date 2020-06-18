from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from test_pg import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=True)
    birthdate = db.Column(db.DateTime)

    def __init__(self, id, name, birthdate):
        self.id = id
        self.name = name
        self.birthdate = birthdate

    # 定义__repr__方法，作用：返回对象的可读字符串
    def __repr__(self):
        return 'id:%s,name:%s,birthdate:%s' % (self.id, self.name, self.birthdate)


# db.create_all()  # 创建表
# db.drop_all()  # 删除表

user1 = Test(1, 'faee', '1987-03-15')
user2 = Test(2, '张三', '2020-06-03')
user3 = Test(3, '@hfj@$%', '2021-02-28:18:35:25')
# db.session.add(user1)
# db.session.add(user2)
# db.session.add_all([user1, user2])
# db.session.add(user3)

# 删除--先查询再删除
# user3 = Test.query.filter_by(id=3).first()
# db.session.delete(user3)

# 修改--先查询再修改
# user = Test.query.filter_by(id=3).first()
# user.name = 'Sovereign'

# 查询
sear = Test.query.all()  # 查询所有用户数据
# print(sear[0])
# print(sear[1].name, sear[2].birthdate)  # 打印选中的数据
# 根据主键查询
sear1 = Test.query.get(1)
# print(sear1)
sear2 = Test.query.count()  # 查询多少用户
# print(sear2)

# 查询name为发faee的数据
sear3 = Test.query.filter(Test.name == 'faee').first()
sear3_1 = Test.query.filter_by(name='faee').all()
# print(sear3.birthdate)
# print(sear3_1)

# 升序和降序排序
sear4 = Test.query.filter().order_by(Test.id.desc()).all()
# print(sear4)
# 查询name以f开头的数据
sear5 = Test.query.filter(Test.name.startswith('f')).first()
# print(sear5.birthdate)
# 查询并，或，非，（and_, or_, not_）
from sqlalchemy import and_
sear6 = Test.query.filter(and_(Test.name == 'Sovereign', Test.id == 3)).first()
# print(sear6.birthdate)
sear7 = Test.query.filter(Test.id.in_([1, 3])).all()
# print(sear7[0].name, sear7[1].birthdate)

db.session.commit()
