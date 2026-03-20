from flask import Blueprint
from .services import (
    get_all_delivery_services,
    get_delivery_by_id_services,
    add_delivery_service,
    update_delivery_by_id_services,
    delete_delivery_by_id_services
)

delivery = Blueprint("delivery", __name__)


@delivery.route("/delivery-management/deliveries", methods=["GET"])
def get_all_deliveries():
    return get_all_delivery_services()


@delivery.route("/delivery-management/delivery", methods=["POST"])
def add_delivery():
    return add_delivery_service()


@delivery.route("/delivery-management/delivery/<int:id_delivery>", methods=["GET"])
def get_delivery_by_id(id_delivery):
    return get_delivery_by_id_services(id_delivery)


@delivery.route("/delivery-management/delivery/<int:id_delivery>", methods=["PUT"])
def update_delivery_by_id(id_delivery):
    return update_delivery_by_id_services(id_delivery)


@delivery.route("/delivery-management/delivery/<int:id_delivery>", methods=["DELETE"])
def delete_delivery_by_id(id_delivery):
    return delete_delivery_by_id_services(id_delivery)