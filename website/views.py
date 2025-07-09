from flask import Flask, Blueprint, render_template, request, redirect, session, url_for
from . import db
from .models import User, Transaction

views = Blueprint("views", __name__)

depts = []
payments = []


# Home page
@views.route("/")
def home():
    username = session.get("username", "مجهول")
    return render_template("index.html", name=username)


# Debt tracker view
@views.route("/debt-tracker")
def debt_tracker():
    username = session.get("username", "مجهول")
    if session.get("username") and session.get("admin") == False:
        user = User.query.get(session["user_id"])
        debts = [i.price for i in user.transactions if bool(i.debt)]
        payments = [i.price for i in user.transactions if not bool(i.debt)]
        t_debts = sum(debts)
        t_payments = sum(payments)
        return render_template(
            "debt tracker.html",
            user=user,
            debts=t_debts,
            paid=t_payments,
            name=username,
        )
    else:
        return redirect(url_for("views.user_login"))


@views.route("/financial-info", methods=["GET"])
def financial_info():
    selected_price_tag = request.args.get("price_tag", default="all")
    selected_year = request.args.get("year", default="all")
    username = session.get("username", "مجهول")
    if session.get("username") and session.get("admin") == False:

        user = User.query.get(session["user_id"])
        reversed_transactions = reversed(user.transactions)
        transactions = list(reversed_transactions)

        years = sorted({t.date[:4] for t in transactions}, reverse=True)
        house_name = "مشورع الوفاء 1"  # this is temporary ...
        return render_template(
            "financial info.html",
            transactions=transactions,
            house_name=house_name,
            name=username,
            years=years,
            selected_year=selected_year,
            selected_price_tag=selected_price_tag,
        )
    else:
        return redirect(url_for("views.user_login"))


# Admin login route
@views.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    global username

    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")

        user = User.query.filter_by(name=name, code=code).first()

        if user and user.admin == True:
            session["admin"] = True
            session["username"] = user.name
            session["code"] = user.code
            username = session["username"]
            return redirect("/admin-dashboard")
        else:
            return render_template("admin login.html", error="Access denied.")
    else:
        return render_template("admin login.html")


@views.route("/user-login", methods=["GET", "POST"])
def user_login():
    global username

    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")

        user = User.query.filter_by(name=name, code=code).first()

        if user:
            session["admin"] = False
            session["username"] = user.name
            session["code"] = user.code
            session["user_id"] = user.id
            username = session["username"]
            return redirect("/debt-tracker")
        else:
            return render_template("user login.html", error="Access denied.")
    else:
        return render_template("user login.html")


@views.route("/admin-dashboard")
def admin_dashboard():
    username = session.get("username", "مجهول")
    if session["admin"]:
        return render_template("admin dashboard.html", name=username)

    else:
        return redirect("/admin-login")


@views.route("/logout")
def logout():
    session.clear()
    return redirect("/")


def add_no_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, private"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response
