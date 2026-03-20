from datetime import datetime
from flask import request, jsonify
from library.extension import db
from library.library_ma import DeliverySchema
from library.model import Delivery

delivery_schema = DeliverySchema()
deliveries_schema = DeliverySchema(many=True)


def add_delivery_service():
    data = request.get_json()
    required_fields = ["id_reservation", "address", "price"]
    if not data:
        return jsonify({"error": "No data"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    try:
        delivery_date = None
        if data.get("delivery_date"):
            delivery_date = datetime.strptime(data["delivery_date"], "%Y-%m-%d")

        new_delivery = Delivery(
            id_reservation=data["id_reservation"],
            address=data["address"],
            price=data["price"],
            created_at=datetime.utcnow(),
            delivery_date=delivery_date,
            status=data.get("status", "pending")
        )
        db.session.add(new_delivery)
        db.session.commit()
        return jsonify(delivery_schema.dump(new_delivery)), 201
    except ValueError:
        db.session.rollback()
        return jsonify({"error": "delivery_date must be YYYY-MM-DD"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def get_all_delivery_services():
    deliveries = Delivery.query.all()
    return jsonify(deliveries_schema.dump(deliveries)), 200


def get_delivery_by_id_services(id_delivery):
    item = Delivery.query.get(id_delivery)
    if not item:
        return jsonify({"message": "Not found delivery"}), 404
    return jsonify(delivery_schema.dump(item)), 200


def update_delivery_by_id_services(id_delivery):
    item = Delivery.query.get(id_delivery)
    data = request.get_json()

    if not item:
        return jsonify({"message": "Not found delivery"}), 404
    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        for field in ["id_reservation", "address", "price", "status"]:
            if field in data:
                setattr(item, field, data[field])

        if "delivery_date" in data:
            item.delivery_date = datetime.strptime(data["delivery_date"], "%Y-%m-%d")

        db.session.commit()
        return jsonify(delivery_schema.dump(item)), 200
    except ValueError:
        db.session.rollback()
        return jsonify({"error": "delivery_date must be YYYY-MM-DD"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def delete_delivery_by_id_services(id_delivery):
    item = Delivery.query.get(id_delivery)
    if not item:
        return jsonify({"message": "Not found delivery"}), 404

    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Delivery deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()