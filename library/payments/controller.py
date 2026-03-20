from flask import Blueprint
from .services import (
    get_all_payment_services,
    get_payment_by_id_services,
    add_payment_service,
    update_payment_by_id_services,
    delete_payment_by_id_services
)

payments = Blueprint("payments", __name__)


@payments.route("/payments-management/payments", methods=["GET"])
def get_all_payments():
    return get_all_payment_services()


@payments.route("/payments-management/payment", methods=["POST"])
def add_payment():
    return add_payment_service()


@payments.route("/payments-management/payment/<int:id_payment>", methods=["GET"])
def get_payment_by_id(id_payment):
    return get_payment_by_id_services(id_payment)


@payments.route("/payments-management/payment/<int:id_payment>", methods=["PUT"])
def update_payment_by_id(id_payment):
    return update_payment_by_id_services(id_payment)


@payments.route("/payments-management/payment/<int:id_payment>", methods=["DELETE"])
def delete_payment_by_id(id_payment):
    return delete_payment_by_id_services(id_payment)