from flask import Blueprint
from .services import (
    get_all_favorite_services,
    get_favorite_by_id_services,
    add_favorite_service,
    delete_favorite_by_id_services,
     get_favorites_by_user_service,
    delete_favorite_by_user_book_service,
    get_favorites_by_user_id_service ,
)

favorites = Blueprint("favorites", __name__)


@favorites.route("/favorites-management/favorites", methods=["GET"])
def get_all_favorites():
    return get_all_favorite_services()


@favorites.route("/favorites-management/favorite", methods=["POST"])
def add_favorite():
    return add_favorite_service()


@favorites.route("/favorites-management/favorite/<int:id_favorite>", methods=["GET"])
def get_favorite_by_id(id_favorite):
    return get_favorite_by_id_services(id_favorite)


@favorites.route("/favorites-management/favorite/<int:id_favorite>", methods=["DELETE"])
def delete_favorite_by_id(id_favorite):
    return delete_favorite_by_id_services(id_favorite)

@favorites.route("/favorites-management/favorites/user/<int:id_user>", methods=["GET"])
def get_favorites_by_user(id_user):
    return get_favorites_by_user_service(id_user)


@favorites.route("/favorites-management/favorite/user/<int:id_user>/book/<int:id_book>", methods=["DELETE"])
def delete_favorite_by_user_book(id_user, id_book):
    return delete_favorite_by_user_book_service(id_user, id_book)

@favorites.route('/favorites-management/favorite/user/<int:id_user>', methods=['GET'])
def get_favorites_by_user_id(id_user):
    return get_favorites_by_user_id_service(id_user)