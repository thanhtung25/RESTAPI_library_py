from flask import Blueprint
from .services import (
    get_all_reservation_services,
    get_reservation_by_id_services,
    add_reservation_service,
    update_reservation_by_id_services,
    delete_reservation_by_id_services
)

reservations = Blueprint("reservations", __name__)


@reservations.route("/reservations-management/reservations", methods=["GET"])
def get_all_reservations():
    return get_all_reservation_services()


@reservations.route("/reservations-management/reservation", methods=["POST"])
def add_reservation():
    return add_reservation_service()


@reservations.route("/reservations-management/reservation/<int:id_reservation>", methods=["GET"])
def get_reservation_by_id(id_reservation):
    return get_reservation_by_id_services(id_reservation)


@reservations.route("/reservations-management/reservation/<int:id_reservation>", methods=["PUT"])
def update_reservation_by_id(id_reservation):
    return update_reservation_by_id_services(id_reservation)


@reservations.route("/reservations-management/reservation/<int:id_reservation>", methods=["DELETE"])
def delete_reservation_by_id(id_reservation):
    return delete_reservation_by_id_services(id_reservation)