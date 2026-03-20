from datetime import datetime
from flask import request, jsonify
from library.extension import db
from library.library_ma import PaymentsSchema
from library.model import Payments

payment_schema = PaymentsSchema()
payments_schema = PaymentsSchema(many=True)


def add_payment_service():
    data = request.get_json()
    required_fields = ["id_user", "payment_type", "amount"]
    if not data:
        return jsonify({"error": "No data"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    if data["payment_type"] == "fine" and "id_fine" not in data:
        return jsonify({"error": "id_fine is required for fine payment"}), 400
    if data["payment_type"] == "delivery" and "id_delivery" not in data:
        return jsonify({"error": "id_delivery is required for delivery payment"}), 400

    try:
        new_payment = Payments(
            id_user=data["id_user"],
            payment_type=data["payment_type"],
            amount=data["amount"],
            id_fine=data.get("id_fine"),
            id_delivery=data.get("id_delivery"),
            payment_date=datetime.utcnow(),
            payment_method=data.get("payment_method"),
            document_number=data.get("document_number"),
            status=data.get("status", "paid")
        )
        db.session.add(new_payment)
        db.session.commit()
        return jsonify(payment_schema.dump(new_payment)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def get_all_payment_services():
    items = Payments.query.all()
    return jsonify(payments_schema.dump(items)), 200


def get_payment_by_id_services(id_payment):
    item = Payments.query.get(id_payment)
    if not item:
        return jsonify({"message": "Not found payment"}), 404
    return jsonify(payment_schema.dump(item)), 200


def update_payment_by_id_services(id_payment):
    item = Payments.query.get(id_payment)
    data = request.get_json()

    if not item:
        return jsonify({"message": "Not found payment"}), 404
    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        for field in [
            "id_user", "id_fine", "id_delivery", "payment_type",
            "amount", "payment_method", "document_number", "status"
        ]:
            if field in data:
                setattr(item, field, data[field])

        db.session.commit()
        return jsonify(payment_schema.dump(item)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def delete_payment_by_id_services(id_payment):
    item = Payments.query.get(id_payment)
    if not item:
        return jsonify({"message": "Not found payment"}), 404

    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Payment deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()