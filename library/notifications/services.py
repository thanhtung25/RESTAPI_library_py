from datetime import datetime
from flask import request, jsonify
from library.extension import db
from library.library_ma import NotificationsSchema
from library.model import Notifications

notification_schema = NotificationsSchema()
notifications_schema = NotificationsSchema(many=True)


def add_notification_service():
    data = request.get_json()
    required_fields = ["id_user", "type", "message"]
    if not data:
        return jsonify({"error": "No data"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    try:
        new_notification = Notifications(
            id_user=data["id_user"],
            type=data["type"],
            message=data["message"],
            sent_at=datetime.utcnow(),
            is_read=data.get("is_read", False)
        )
        db.session.add(new_notification)
        db.session.commit()
        return jsonify(notification_schema.dump(new_notification)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def get_all_notification_services():
    notifications = Notifications.query.all()
    return jsonify(notifications_schema.dump(notifications)), 200


def get_notification_by_id_services(id_notification):
    notification = Notifications.query.get(id_notification)
    if not notification:
        return jsonify({"message": "Not found notification"}), 404
    return jsonify(notification_schema.dump(notification)), 200


def update_notification_by_id_services(id_notification):
    notification = Notifications.query.get(id_notification)
    data = request.get_json()

    if not notification:
        return jsonify({"message": "Not found notification"}), 404
    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        for field in ["id_user", "type", "message", "is_read"]:
            if field in data:
                setattr(notification, field, data[field])

        db.session.commit()
        return jsonify(notification_schema.dump(notification)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def delete_notification_by_id_services(id_notification):
    notification = Notifications.query.get(id_notification)
    if not notification:
        return jsonify({"message": "Not found notification"}), 404

    try:
        db.session.delete(notification)
        db.session.commit()
        return jsonify({"message": "Notification deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()