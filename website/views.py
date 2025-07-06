from flask import Flask, Blueprint, render_template, request, redirect, session
from . import db
from .models import User, Transaction

views = Blueprint("views", __name__)

# Sample values (temporary for demonstration)
depts = 3000000
paid = 2500000

prev_items = [
    {"name": "سمنت", "price": 150000},
    {"name": "لبخ", "price": 125000},
]


# Home page
@views.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# Debt tracker view
@views.route("/debt-tracker")
def debt_tracker():
    return render_template(
        "debt tracker.html", depts=depts, paid=paid, prev_items=prev_items
    )


# Financial information page showing transactions
@views.route("/financial-info")
def financial_info():
    debts = Transaction.query.filter_by(debt="1").all()
    payments = Transaction.query.filter_by(debt="False").all()
    return render_template("financial info.html", debts=debts, payment=payments)


# Admin login route
@views.route("/admin-page", methods=["GET", "POST"])
def admin_page():
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")

        user = User.query.filter_by(name=name, code=code).first()

        if user and user.admin == "1":
            session["admin"] = True
            session["username"] = user.name
            return redirect("/admin-dashboard")
        else:
            return render_template("admin login.html", error="Access denied.")

    return render_template("admin login.html")


# Admin dashboard - protected
@views.route("/admin-dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect("/admin-page")
    return render_template("admin_dashboard.html")


# Logout route
@views.route("/logout")
def logout():
    session.clear()
    return redirect("/")
