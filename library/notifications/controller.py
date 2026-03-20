from flask import Blueprint
from .services import (
    get_all_notification_services,
    get_notification_by_id_services,
    add_notification_service,
    update_notification_by_id_services,
    delete_notification_by_id_services
)

notifications = Blueprint("notifications", __name__)


@notifications.route("/notifications-management/notifications", methods=["GET"])
def get_all_notifications():
    return get_all_notification_services()


@notifications.route("/notifications-management/notification", methods=["POST"])
def add_notification():
    return add_notification_service()


@notifications.route("/notifications-management/notification/<int:id_notification>", methods=["GET"])
def get_notification_by_id(id_notification):
    return get_notification_by_id_services(id_notification)


@notifications.route("/notifications-management/notification/<int:id_notification>", methods=["PUT"])
def update_notification_by_id(id_notification):
    return update_notification_by_id_services(id_notification)


@notifications.route("/notifications-management/notification/<int:id_notification>", methods=["DELETE"])
def delete_notification_by_id(id_notification):
    return delete_notification_by_id_services(id_notification)