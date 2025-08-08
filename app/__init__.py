from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from flask import Response
from prometheus_flask_exporter import PrometheusMetrics



db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    metrics = PrometheusMetrics(app)
    print("Rutas registradas:", [str(r) for r in app.url_map.iter_rules()])


    print("Rutas registradas:", [rule.rule for rule in app.url_map.iter_rules()])

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    Session(app)

    # Configure login manager
    login_manager.login_view = "main.login"
    login_manager.login_message = "Please log in to access this page."

    # Load the user from the database
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()



    with app.app_context():
        db.create_all()




    return app

