from datetime import datetime
from flask import request, jsonify
from library.extension import db
from library.library_ma import ReservationsSchema
from library.model import Reservations

reservation_schema = ReservationsSchema()
reservations_schema = ReservationsSchema(many=True)


def add_reservation_service():
    data = request.get_json()
    required_fields = ["id_user", "id_book"]

    if not data:
        return jsonify({"message": "No data"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"{field} is required"}), 400

    try:
        existing_reservation = Reservations.query.filter(
            Reservations.id_user == data["id_user"],
            Reservations.id_book == data["id_book"],
            Reservations.status != "cancelled"
        ).first()

        if existing_reservation:
            return jsonify({"message": "Книга уже в корзине."}), 400

        expiration_date = None
        if data.get("expiration_date"):
            expiration_date = datetime.strptime(data["expiration_date"], "%Y-%m-%d")

        new_reservation = Reservations(
            id_user=data["id_user"],
            id_book=data["id_book"],
            reservation_date=datetime.utcnow(),
            expiration_date=expiration_date,
            comment=data.get("comment"),
            status=data.get("status", "pending")
        )

        db.session.add(new_reservation)
        db.session.commit()

        return jsonify(reservation_schema.dump(new_reservation)), 201

    except ValueError:
        db.session.rollback()
        return jsonify({"message": "expiration_date must be YYYY-MM-DD"}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

    finally:
        db.session.close()

def get_all_reservation_services():
    reservations = Reservations.query.all()
    return jsonify(reservations_schema.dump(reservations)), 200


def get_reservation_by_id_services(id_reservation):
    reservation = Reservations.query.get(id_reservation)
    if not reservation:
        return jsonify({"message": "Not found reservation"}), 404
    return jsonify(reservation_schema.dump(reservation)), 200


def update_reservation_by_id_services(id_reservation):
    reservation = Reservations.query.get(id_reservation)
    data = request.get_json()

    if not reservation:
        return jsonify({"message": "Not found reservation"}), 404
    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        for field in ["id_user", "id_book", "comment", "status"]:
            if field in data:
                setattr(reservation, field, data[field])

        if "expiration_date" in data:
            reservation.expiration_date = datetime.strptime(data["expiration_date"], "%Y-%m-%d")

        db.session.commit()
        return jsonify(reservation_schema.dump(reservation)), 200
    except ValueError:
        db.session.rollback()
        return jsonify({"error": "expiration_date must be YYYY-MM-DD"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def delete_reservation_by_id_services(id_reservation):
    reservation = Reservations.query.get(id_reservation)
    if not reservation:
        return jsonify({"message": "Not found reservation"}), 404

    try:
        db.session.delete(reservation)
        db.session.commit()
        return jsonify({"message": "Reservation deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()

def get_reservations_by_user_service(id_user):
    try:
        reservations = Reservations.query.filter_by(id_user=id_user).all()

        if not reservations:
            return jsonify({
                "message": "No reservations found for this user"
            }), 404

        return jsonify(reservations_schema.dump(reservations)), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500