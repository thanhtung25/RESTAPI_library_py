from flask import Blueprint
from .services import (
    get_all_category_services,
    get_category_by_id_services,
    add_category_service,
    update_category_by_id_services,
    delete_category_by_id_services
)

categories = Blueprint("categories", __name__)


@categories.route("/categories-management/categories", methods=["GET"])
def get_all_categories():
    return get_all_category_services()


@categories.route("/categories-management/category", methods=["POST"])
def add_category():
    return add_category_service()


@categories.route("/categories-management/category/<int:id_category>", methods=["GET"])
def get_category_by_id(id_category):
    return get_category_by_id_services(id_category)


@categories.route("/categories-management/category/<int:id_category>", methods=["PUT"])
def update_category_by_id(id_category):
    return update_category_by_id_services(id_category)


@categories.route("/categories-management/category/<int:id_category>", methods=["DELETE"])
def delete_category_by_id(id_category):
    return delete_category_by_id_services(id_category)