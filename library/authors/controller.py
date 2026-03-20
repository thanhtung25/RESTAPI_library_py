from flask import Blueprint
from .services import (
    get_all_author_services,
    get_author_by_id_services,
    add_author_service,
    update_author_by_id_services,
    delete_author_by_id_services
)

authors = Blueprint("authors", __name__)


@authors.route("/authors-management/authors", methods=["GET"])
def get_all_authors():
    return get_all_author_services()


@authors.route("/authors-management/author", methods=["POST"])
def add_author():
    return add_author_service()


@authors.route("/authors-management/author/<int:id_author>", methods=["GET"])
def get_author_by_id(id_author):
    return get_author_by_id_services(id_author)


@authors.route("/authors-management/author/<int:id_author>", methods=["PUT"])
def update_author_by_id(id_author):
    return update_author_by_id_services(id_author)


@authors.route("/authors-management/author/<int:id_author>", methods=["DELETE"])
def delete_author_by_id(id_author):
    return delete_author_by_id_services(id_author)