from flask import Flask

from .books.controller import books
from .book_copies.controller import book_copies
from .users.controller import users
from .categories.controller import categories
from .authors.controller import authors
from .loans.controller import loans
from .favorites.controller import favorites
from .fines.controller import fines
from .notifications.controller import notifications
from .reservations.controller import reservations
from .delivery.controller import delivery
from .payments.controller import payments
from .extension import db, ma
from .model import (
    Users, Books, BookCopies, Categories, Authors,
    Loans, Favorites, Fines, Notifications,
    Reservations, Delivery, Payments
)
import os


def create_db(app):
    with app.app_context():
        
        db_uri = app.config["SQLALCHEMY_DATABASE_URI"]

        if db_uri.startswith("sqlite:///"):
            db_path = db_uri.replace("sqlite:///", "")

            if not os.path.exists(db_path):
                db.create_all()
                print("Created DB:", db_path)
            else:
                print("DB exists:", db_path)
        else:
            db.create_all()


def create_app(config_file="config.py"):

    app = Flask(__name__)

    # load config đúng path
    base_dir = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(base_dir, config_file)

    app.config.from_pyfile(config_path)

    # init db sau khi load config
    db.init_app(app)
    ma.init_app(app)



    create_db(app)
    app.register_blueprint(books)
    app.register_blueprint(book_copies)
    app.register_blueprint(users)
    app.register_blueprint(categories)
    app.register_blueprint(authors)
    app.register_blueprint(loans)
    app.register_blueprint(favorites)
    app.register_blueprint(fines)
    app.register_blueprint(notifications)
    app.register_blueprint(reservations)
    app.register_blueprint(delivery)
    app.register_blueprint(payments)
    return app