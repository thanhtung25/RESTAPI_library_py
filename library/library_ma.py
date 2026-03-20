from .extension import ma
from .model import (
    Users, Categories, Authors, Books, BookCopies,
    Loans, Fines, Notifications, Reservations,
    Favorites, Delivery, Payments
)


class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True
        include_fk = True


class CategoriesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Categories
        load_instance = True
        include_fk = True


class AuthorsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Authors
        load_instance = True
        include_fk = True


class BooksSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Books
        load_instance = True
        include_fk = True


class BookCopiesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookCopies
        load_instance = True
        include_fk = True


class LoansSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Loans
        load_instance = True
        include_fk = True


class FinesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Fines
        load_instance = True
        include_fk = True


class NotificationsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Notifications
        load_instance = True
        include_fk = True


class ReservationsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reservations
        load_instance = True
        include_fk = True


class FavoritesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Favorites
        load_instance = True
        include_fk = True


class DeliverySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Delivery
        load_instance = True
        include_fk = True


class PaymentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Payments
        load_instance = True
        include_fk = True