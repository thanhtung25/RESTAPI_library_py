from datetime import datetime
from flask import request, jsonify
from library.extension import db
from library.library_ma import FinesSchema
from library.model import Fines

fine_schema = FinesSchema()
fines_schema = FinesSchema(many=True)


def add_fine_service():
    data = request.get_json()
    required_fields = ["id_loan", "amount"]

    if not data:
        return jsonify({"error": "No data"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    try:
        created_at = None
        if data.get("created_at"):
            created_at = datetime.strptime(data["created_at"], "%Y-%m-%d")

        new_fine = Fines(
            id_loan=data["id_loan"],
            amount=data["amount"],
            reason=data.get("reason"),
            created_at=created_at,
            status=data.get("status", "unpaid")
        )

        db.session.add(new_fine)
        db.session.commit()
        return jsonify(fine_schema.dump(new_fine)), 201

    except ValueError:
        db.session.rollback()
        return jsonify({"error": "Date format must be YYYY-MM-DD"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def get_all_fine_services():
    fines = Fines.query.all()
    return jsonify(fines_schema.dump(fines)), 200


def get_fine_by_id_services(id_fine):
    fine = Fines.query.get(id_fine)
    if not fine:
        return jsonify({"message": "Not found fine"}), 404
    return jsonify(fine_schema.dump(fine)), 200


def update_fine_by_id_services(id_fine):
    fine = Fines.query.get(id_fine)
    data = request.get_json()

    if not fine:
        return jsonify({"message": "Not found fine"}), 404
    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        for field in ["id_loan", "amount", "reason", "status"]:
            if field in data:
                setattr(fine, field, data[field])

        if "created_at" in data:
            fine.created_at = datetime.strptime(data["created_at"], "%Y-%m-%d")

        db.session.commit()
        return jsonify(fine_schema.dump(fine)), 200

    except ValueError:
        db.session.rollback()
        return jsonify({"error": "Date format must be YYYY-MM-DD"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def delete_fine_by_id_services(id_fine):
    fine = Fines.query.get(id_fine)
    if not fine:
        return jsonify({"message": "Not found fine"}), 404

    try:
        db.session.delete(fine)
        db.session.commit()
        return jsonify({"message": "Fine deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()