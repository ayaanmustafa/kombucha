from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from kombucha.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
#This tells the app where the login route is located. Login is the function name
login_manager.login_view = 'users.login'
#Adds a categroy to the login message, info is the name of a type of alert
login_manager.login_message_category = 'info'
#create constants for mail
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    #pass in Config app file
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    #you are importing the blueprint instance now instead of the routes.py page
    from kombucha.users.routes import users
    from kombucha.posts.routes import posts
    from kombucha.main.routes import main
    from kombucha.errors.handlers import errors

    #blueprint must be registered
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app


