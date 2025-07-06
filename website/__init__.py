from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "SAJAD2009"

    # Database configuration (using instance folder for SQLite)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        app.instance_path, "app.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from .views import views

    app.register_blueprint(views)

    # Import and create database tables
    from .models import User, Transaction

    with app.app_context():
        db.create_all()

    return app
