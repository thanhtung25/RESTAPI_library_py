from flask import Blueprint
from .services import (
    get_all_user_services,
    get_user_by_id_services,
    add_user_service,
    update_user_by_id_services,
    delete_user_by_id_services,
    login_services,
    upload_avatar_service
)

users = Blueprint("users", __name__)


@users.route("/users-management/users", methods=["GET"])
def get_all_users():
    return get_all_user_services()


@users.route("/users-management/user", methods=["POST"])
def add_user():
    return add_user_service()


@users.route("/users-management/user/<int:id_user>", methods=["GET"])
def get_user_by_id(id_user):
    return get_user_by_id_services(id_user)


@users.route("/users-management/user/<int:id_user>", methods=["PUT"])
def update_user_by_id(id_user):
    return update_user_by_id_services(id_user)


@users.route("/users-management/user/<int:id_user>", methods=["DELETE"])
def delete_user_by_id(id_user):
    return delete_user_by_id_services(id_user)

@users.route("/login", methods=["POST"])
def login():
    return login_services()

@users.route("/users-management/user/<int:id_user>/avatar", methods=["PUT"])
def upload_avatar(id_user):
    return upload_avatar_service(id_user)