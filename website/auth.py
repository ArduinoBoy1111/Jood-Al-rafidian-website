from flask import Flask, Blueprint, render_template, request

views = Blueprint("views", __name__)


@views.route("/login")
def home():
    return render_template("login.html")
