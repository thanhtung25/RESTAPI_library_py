from flask import Blueprint
from .services import (
    get_all_book_copy_services,
    get_book_copy_by_id_services,
    delete_book_copy_by_id_services,
    update_book_copy_by_id_services,
    add_book_copy_service,
    get_book_copy_by_id_book_services
)

book_copies = Blueprint("book_copies", __name__)


@book_copies.route("/book_copies-management/book_copies", methods=["GET"])
def get_all_book_copies():
    return get_all_book_copy_services()


@book_copies.route("/book_copies-management/book_copy", methods=["POST"])
def add_book_copy():
    return add_book_copy_service()


@book_copies.route("/book_copies-management/book_copy/<int:id_copy>", methods=["GET"])
def get_book_copy_by_id(id_copy):
    return get_book_copy_by_id_services(id_copy)


@book_copies.route("/book_copies-management/book_copy/<int:id_copy>", methods=["PUT"])
def update_book_copy_by_id(id_copy):
    return update_book_copy_by_id_services(id_copy)


@book_copies.route("/book_copies-management/book_copy/<int:id_copy>", methods=["DELETE"])
def delete_book_copy_by_id(id_copy):
    return delete_book_copy_by_id_services(id_copy)

@book_copies.route("/book_copies-management/book_copies/book/<int:id_book>", methods=["GET"])
def get_book_copy_by_id_book(id_book):
    return get_book_copy_by_id_book_services(id_book)