from flask import Blueprint
from .services import (
    get_all_loan_services,
    get_loan_by_id_services,
    add_loan_service,
    update_loan_by_id_services,
    delete_loan_by_id_services
)

loans = Blueprint("loans", __name__)


@loans.route("/loans-management/loans", methods=["GET"])
def get_all_loans():
    return get_all_loan_services()


@loans.route("/loans-management/loan", methods=["POST"])
def add_loan():
    return add_loan_service()


@loans.route("/loans-management/loan/<int:id_loan>", methods=["GET"])
def get_loan_by_id(id_loan):
    return get_loan_by_id_services(id_loan)


@loans.route("/loans-management/loan/<int:id_loan>", methods=["PUT"])
def update_loan_by_id(id_loan):
    return update_loan_by_id_services(id_loan)


@loans.route("/loans-management/loan/<int:id_loan>", methods=["DELETE"])
def delete_loan_by_id(id_loan):
    return delete_loan_by_id_services(id_loan)