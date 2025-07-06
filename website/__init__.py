from flask import Flask
<<<<<<< HEAD
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
=======
>>>>>>> f88e617cec8518451e328326facaf907971b4757
=======
>>>>>>> f88e617cec8518451e328326facaf907971b4757


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "SAJAD2009"
<<<<<<< HEAD
<<<<<<< HEAD
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        app.instance_path, "app.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
=======
>>>>>>> f88e617cec8518451e328326facaf907971b4757
=======
>>>>>>> f88e617cec8518451e328326facaf907971b4757

    from .views import views

    app.register_blueprint(views)

<<<<<<< HEAD
<<<<<<< HEAD
    from . import models
    from .models import User, Transaction

    with app.app_context():
        db.create_all()

    return app
=======
    app.run(debug=True)
>>>>>>> f88e617cec8518451e328326facaf907971b4757
=======
    app.run(debug=True)
>>>>>>> f88e617cec8518451e328326facaf907971b4757
