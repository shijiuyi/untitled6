from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://' \
                                        'postgres:123456@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

association_table = db.Table('association',
                             db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                             db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
                             db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
                             )


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    work = db.Column(db.String(64))

    def __repr__(self):
        return 'name:{name} work:{work}'.format(name=self.name, work=self.work)

    customer_to_product = db.relationship('Product',
                                          secondary=association_table,
                                          backref='product_to_customer',
                                          lazy='dynamic')


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    price = db.Column(db.Float)

    def __repr__(self):
        return 'name:{name} price:{price}'.format(name=self.name, price=self.price)


# db.create_all()
# db.drop_all()
# 添加Customer表的数据
# cus1 = Customer(id=1, name="刘老板", work="某某大老板")
# cus2 = Customer(id=2, name="石教授", work="某某大学教授")
# cus3 = Customer(id=3, name="郝老师", work="某某高中老师")
# cus4 = Customer(id=4, name="神码学者", work="某某深吗研究")
# db.session.add_all([cus1, cus2, cus3, cus4])
# db.session.commit()

# 添加Product表中的数据
# pro1 = Product(id=1, name="豪华大餐", price=88888)
# pro2 = Product(id=2, name="一条龙服务", price=66666.666)
# pro3 = Product(id=3, name="快餐", price=9.99)
# pro4 = Product(id=4, name="电子高科技", price=188888)
# pro5 = Product(id=5, name="水", price=2.0)
# db.session.add_all([pro1, pro2, pro3, pro4, pro5])
# db.session.commit()

# 查找顾客表中的为key的数据
key = "刘老板"
cstm1 = Customer.query.filter_by(name=key).first()
cstm2 = Customer.query.filter_by(name=key).all()
print(cstm1, type(cstm1))
print(cstm2, type(cstm2))

# 查找顾客为key的数据所点的product名称
prdt = cstm1.customer_to_product
print(prdt, type(prdt))

for i in prdt:
    print(i.name, i.price)
