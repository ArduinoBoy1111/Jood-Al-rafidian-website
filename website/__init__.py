from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "SAJAD2009"

    from .views import views

    app.register_blueprint(views)

    app.run(debug=True)
