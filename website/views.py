from flask import Flask, Blueprint, render_template, request
from . import db
from .models import User, Transaction

views = Blueprint("views", __name__)

depts = 3000000
paid = 2500000


@views.route("/", methods=["GET"])
def home():
    return render_template("index.html")


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
