from flask import Blueprint
from .services import (
    get_all_fine_services,
    get_fine_by_id_services,
    add_fine_service,
    update_fine_by_id_services,
    delete_fine_by_id_services
)

fines = Blueprint("fines", __name__)


@fines.route("/fines-management/fines", methods=["GET"])
def get_all_fines():
    return get_all_fine_services()


@fines.route("/fines-management/fine", methods=["POST"])
def add_fine():
    return add_fine_service()


@fines.route("/fines-management/fine/<int:id_fine>", methods=["GET"])
def get_fine_by_id(id_fine):
    return get_fine_by_id_services(id_fine)


@fines.route("/fines-management/fine/<int:id_fine>", methods=["PUT"])
def update_fine_by_id(id_fine):
    return update_fine_by_id_services(id_fine)


@fines.route("/fines-management/fine/<int:id_fine>", methods=["DELETE"])
def delete_fine_by_id(id_fine):
    return delete_fine_by_id_services(id_fine)