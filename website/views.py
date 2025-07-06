from flask import Flask, Blueprint, render_template, request
<<<<<<< HEAD
from . import db
from .models import User, Transaction
=======
>>>>>>> f88e617cec8518451e328326facaf907971b4757

views = Blueprint("views", __name__)

depts = 3000000
paid = 2500000
<<<<<<< HEAD


@views.route("/", methods=["GET"])
=======
prev_items = [
    {"name": "سمنت", "price": 150000},
    {"name": "لبخ", "price": 125000},
]


@views.route("/")
>>>>>>> f88e617cec8518451e328326facaf907971b4757
def home():
    return render_template("index.html")


<<<<<<< HEAD
@views.route("/debt-tracker")
def dept_tracker():
    return render_template("debt tracker.html", depts=depts, paid=paid)


@views.route("/financial-info")
def financial_info():
    debts = Transaction.query.filter_by(debt="1")
    payments = Transaction.query.filter_by(debt="False")

    return render_template("financial info.html", debts=debts, payment=payments)


@views.route("/admin-page", methods=["GET", "POST"])
def admin_page():
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        if db.Query.filter_by(name=name, code=code).first():
            user = db.Query.filter_by(name=name, code=code).first()
            if user.admin == "1":
                pass
    return render_template("admin login.html")
=======
@views.route("/dept-tracker")
def dept_tracker():
    return render_template(
        "debt tracker.html", depts=depts, paid=paid, prev_items=prev_items
    )
>>>>>>> f88e617cec8518451e328326facaf907971b4757
