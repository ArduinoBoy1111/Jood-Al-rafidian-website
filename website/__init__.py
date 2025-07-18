from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import os
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    load_dotenv()  # Load .env variables

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "SAJAD2009"
    app.permanent_session_lifetime = timedelta(weeks=260)
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

    # Fetch credentials from .env
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .views import views
    from .models import User, Transaction

    app.register_blueprint(views)

    with app.app_context():
        db.create_all()

        if not User.query.filter_by(admin=True).first():
            admin = User(name="admin", code="SAJAD2009", project_name="", admin=True)
            db.session.add(admin)
            db.session.commit()

    return app
