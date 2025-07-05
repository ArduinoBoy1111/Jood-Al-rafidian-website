from flask import Flask, Blueprint, render_template, request

views = Blueprint("views", __name__)

depts = 3000000
paid = 2500000
prev_items = [
    {"name": "سمنت", "price": 150000},
    {"name": "لبخ", "price": 125000},
]


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/dept-tracker")
def dept_tracker():
    return render_template(
        "debt tracker.html", depts=depts, paid=paid, prev_items=prev_items
    )
