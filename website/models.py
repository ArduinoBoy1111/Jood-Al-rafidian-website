from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(100), unique=True, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    transactions = db.relationship("Transaction", backref="author", lazy=True)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    debt = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
