from flask import Flask, Blueprint, render_template, request, redirect, session
from . import db
from .models import User, Transaction

views = Blueprint("views", __name__)

# Sample values (temporary for demonstration)
depts = 3000000
paid = 2500000


# Home page
@views.route("/")
def home():
    return render_template("index.html")


# Debt tracker view
@views.route("/debt-tracker")
def debt_tracker():
    return render_template("debt tracker.html", depts=depts, paid=paid)


# Financial information page showing transactions
@views.route("/financial-info")
def financial_info():
    debts = Transaction.query.filter_by(debt="True").all()
    payments = Transaction.query.filter_by(debt="False").all()
    return render_template("financial info.html", debts=debts, payment=payments)


# Admin login route
@views.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")

        user = User.query.filter_by(name=name, code=code).first()

        if user and user.admin == True:
            session["admin"] = True
            session["username"] = user.name
            session["code"] = user.code

            return redirect("/admin-dashboard")
        else:
            return render_template("admin login.html", error="Access denied.")
    else:
        return render_template("admin login.html")


@views.route("/user-login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")

        user = User.query.filter_by(name=name, code=code).first()

        if user:
            session["admin"] = False
            session["username"] = user.name
            session["code"] = user.code
            session["user_id"] = user.id

            return redirect("/debt-tracker")
        else:
            return render_template("user login.html", error="Access denied.")
    else:
        return render_template("user login.html")


@views.route("/admin-dashboard")
def admin_dashboard():
    if session["admin"]:
        return render_template("admin dashboard.html")

    else:
        return redirect("/admin-login")
