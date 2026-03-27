from .extension import db
from datetime import datetime


class Users(db.Model):

    id_user = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    birth_day = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    phone = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="reader")
    status = db.Column(db.String(50), default="active")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    library_card = db.Column(db.String(100), unique=True, nullable=True)
    address = db.Column(db.String(255), nullable=True)
    avatar_url = db.Column(db.String(255), nullable=True)

    def __init__(
        self,
        full_name,
        birth_day=None,
        gender=None,
        email=None,
        phone=None,
        username=None,
        password=None,
        role="reader",
        status="active",
        created_at=None,
        library_card=None,
        address=None,
        avatar_url=None
    ):
        if role not in ["reader", "librarian"]:
            raise ValueError("role must be 'reader' or 'librarian'")

        self.full_name = full_name
        self.birth_day = birth_day
        self.gender = gender
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password
        self.role = role
        self.status = status
        self.created_at = created_at if created_at else datetime.utcnow()
        self.library_card = library_card
        self.address = address
        self.avatar_url = avatar_url

class Categories(db.Model):

    id_category = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

class Authors(db.Model):

    id_author = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.Text, nullable=True)

    def __init__(self, full_name, biography=None):
        self.full_name = full_name
        self.biography = biography

class Books(db.Model):

    id_book = db.Column(db.Integer, primary_key=True)
    id_category = db.Column(db.Integer, db.ForeignKey("categories.id_category"), nullable=False)
    id_author = db.Column(db.Integer, db.ForeignKey("authors.id_author"), nullable=False)

    title = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(50), unique=True, nullable=True)
    language = db.Column(db.String(50), nullable=True)
    publish_year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(
        self,
        id_category,
        id_author,
        title,
        isbn=None,
        language=None,
        publish_year=None,
        description=None,
        image_url=None,
        created_at=None
    ):
        self.id_category = id_category
        self.id_author = id_author
        self.title = title
        self.isbn = isbn
        self.language = language
        self.publish_year = publish_year
        self.description = description
        self.image_url = image_url
        self.created_at = created_at if created_at else datetime.utcnow()

class BookCopies(db.Model):

    id_copy = db.Column(db.Integer, primary_key=True)
    id_book = db.Column(db.Integer, db.ForeignKey("books.id_book"), nullable=False)
    barcode = db.Column(db.String(100), unique=True, nullable=False)
    qr_code = db.Column(db.String(100), unique=True, nullable=True)
    location = db.Column(db.String(100), nullable=True)
    received_date = db.Column(db.Date, nullable=True)
    condition = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), nullable=False, default="available")

    def __init__(
        self,
        id_book,
        barcode,
        qr_code=None,
        location=None,
        received_date=None,
        condition=None,
        status="available"
    ):
        self.id_book = id_book
        self.barcode = barcode
        self.qr_code = qr_code
        self.location = location
        self.received_date = received_date
        self.condition = condition
        self.status = status

class Loans(db.Model):

    id_loan = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id_user"), nullable=False)
    id_copy = db.Column(db.Integer, db.ForeignKey("book_copies.id_copy"), nullable=False)

    issue_date = db.Column(db.Date, nullable=True)
    return_date = db.Column(db.Date, nullable=False)
    actual_return_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(50), nullable=False, default="borrowed")
    renewal_count = db.Column(db.Integer, nullable=False, default=0)

    def __init__(
        self,
        id_user,
        id_copy,
        issue_date,
        return_date,
        actual_return_date=None,
        status="borrowed",
        renewal_count=0
    ):
        self.id_user = id_user
        self.id_copy = id_copy
        self.issue_date = issue_date
        self.return_date = return_date
        self.actual_return_date = actual_return_date
        self.status = status
        self.renewal_count = renewal_count

class Fines(db.Model):

    id_fine = db.Column(db.Integer, primary_key=True)
    id_loan = db.Column(db.Integer, db.ForeignKey("loans.id_loan"), nullable=False)

    amount = db.Column(db.Float, nullable=False, default=0)
    reason = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False, default="unpaid")

    def __init__(self, id_loan, amount=0, reason=None, created_at=None, status="unpaid"):
        self.id_loan = id_loan
        self.amount = amount
        self.reason = reason
        self.created_at = created_at if created_at else datetime.utcnow()
        self.status = status

class Notifications(db.Model):

    id_notification = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id_user"), nullable=False)

    type = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)

    def __init__(self, id_user, type, message, sent_at=None, is_read=False):
        self.id_user = id_user
        self.type = type
        self.message = message
        self.sent_at = sent_at if sent_at else datetime.utcnow()
        self.is_read = is_read

class Reservations(db.Model):

    id_reservation = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id_user"), nullable=False)
    id_book = db.Column(db.Integer, db.ForeignKey("books.id_book"), nullable=False)

    reservation_date = db.Column(db.DateTime, default=datetime.utcnow)
    expiration_date = db.Column(db.DateTime, nullable=True)
    comment = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), nullable=False, default="pending")

    def __init__(
        self,
        id_user,
        id_book,
        reservation_date=None,
        expiration_date=None,
        comment=None,
        status="pending"
    ):
        self.id_user = id_user
        self.id_book = id_book
        self.reservation_date = reservation_date if reservation_date else datetime.utcnow()
        self.expiration_date = expiration_date
        self.comment = comment
        self.status = status

class Favorites(db.Model):

    id_favorite = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id_user"), nullable=False)
    id_book = db.Column(db.Integer, db.ForeignKey("books.id_book"), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id_user, id_book, created_at=None):
        self.id_user = id_user
        self.id_book = id_book
        self.created_at = created_at if created_at else datetime.utcnow()

class Delivery(db.Model):

    id_delivery = db.Column(db.Integer, primary_key=True)
    id_reservation = db.Column(db.Integer, db.ForeignKey("reservations.id_reservation"), nullable=False, unique=True)

    address = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    delivery_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), nullable=False, default="pending")

    def __init__(
        self,
        id_reservation,
        address,
        price=0,
        created_at=None,
        delivery_date=None,
        status="pending"
    ):
        self.id_reservation = id_reservation
        self.address = address
        self.price = price
        self.created_at = created_at if created_at else datetime.utcnow()
        self.delivery_date = delivery_date
        self.status = status

class Payments(db.Model):
    id_payment = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id_user"), nullable=False)
    id_fine = db.Column(db.Integer, db.ForeignKey("fines.id_fine"), nullable=True, unique=True)
    id_delivery = db.Column(db.Integer, db.ForeignKey("delivery.id_delivery"), nullable=True, unique=True)

    payment_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False, default=0)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    payment_method = db.Column(db.String(50), nullable=True)
    document_number = db.Column(db.String(100), unique=True, nullable=True)
    status = db.Column(db.String(50), nullable=False, default="paid")

    def __init__(
        self,
        id_user,
        payment_type,
        amount=0,
        id_fine=None,
        id_delivery=None,
        payment_date=None,
        payment_method=None,
        document_number=None,
        status="paid"
    ):
        if payment_type not in ["fine", "delivery"]:
            raise ValueError("payment_type must be 'fine' or 'delivery'")

        if payment_type == "fine" and not id_fine:
            raise ValueError("id_fine is required when payment_type is 'fine'")

        if payment_type == "delivery" and not id_delivery:
            raise ValueError("id_delivery is required when payment_type is 'delivery'")

        self.id_user = id_user
        self.id_fine = id_fine
        self.id_delivery = id_delivery
        self.payment_type = payment_type
        self.amount = amount
        self.payment_date = payment_date if payment_date else datetime.utcnow()
        self.payment_method = payment_method
        self.document_number = document_number
        self.status = status
