from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://' \
                                        'postgres:123456@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class Classes(db.Model):
    __tablename__ = 'classes'
    class_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    classname = db.Column(db.String(64))
    location = db.Column(db.Text)
    leader = db.Column(db.String(64))
    remark = db.Column(db.Text)

    # 在此申明Classes类与Students类具备指向关系，且具体的关联是通过
    # 外键db.ForeignKey这个绑定的
    user_relate_article = db.relationship('Students', backref='student_relate_class', lazy='dynamic')
    """
        第一个参数：为对应参照的类名"Students"
        第二个参数：backref为类Students申明新的属性（这个属性方便在2个表格之间互相指向）
        第三个参数：lazy决定了什么时候SQLALchemy从数据库中加载数据
    """


class Students(db.Model):
    __tablename__ = 'students'
    stu_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stu_name = db.Column(db.String(64))
    gender = db.Column(db.String(32))
    stu_age = db.Column(db.Integer)
    remark = db.Column(db.Text)
    # 指定classID这个字段来源于classes表格的外键，指向方式：表名 + 字段名（表名）
    cls_id = db.Column(db.Integer, db.ForeignKey("classes.class_id"))


# db.create_all()
# db.drop_all()

# 一对多查询
key = "奥代"
stu = Students.query.filter_by(stu_name=key).first()
clsname = stu.student_relate_class.classname
print(clsname)

key = "sovereign"
stu = Students.query.filter_by(stu_name=key).first()
rem = stu.remark
print(rem)

info = stu.student_relate_class.remark, stu.student_relate_class.location, stu.student_relate_class.classname
print(info)  # 打印查询的多个结果

key = "stone"
stu = Students.query.filter_by(stu_name=key).first()
stu_loc = stu.student_relate_class.location
print(stu_loc)

all_mes = stu.stu_age, stu.remark, stu.gender, stu.stu_name
print(all_mes)

key = "1"
gen = Students.query.filter_by(gender=key).all()
print(gen[0].remark, gen[1].stu_name)

sfaa = Students.query.all()
print(sfaa)
