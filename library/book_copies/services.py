from library.extension import db
from library.library_ma import BookCopiesSchema
from library.model import BookCopies
from flask import request, jsonify
from datetime import datetime
book_copy_schema = BookCopiesSchema()
book_copies_schema = BookCopiesSchema(many=True)


def add_book_copy_service():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400
    required_fields = [
        "id_book",
        "barcode",
        "qr_code",
        "location",
        "received_date",
        "condition",
        "status"
    ]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400
    try:
        received_date = datetime.strptime(data["received_date"], "%Y-%m-%d").date()

        new_book_copy = BookCopies(
            data["id_book"],
            data["barcode"],
            data["qr_code"],
            data["location"],
            received_date,
            data["condition"],
            data["status"]
        )
        db.session.add(new_book_copy)
        db.session.commit()
        return jsonify(book_copy_schema.dump(new_book_copy)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": str(e)
        }), 500
    

def get_book_copy_by_id_services(id_copy):
    book_copy = BookCopies.query.get(id_copy)
    if book_copy:
        return book_copy_schema.jsonify(book_copy)
    else:
        return jsonify({"message": "Not found book copy "}) , 404

def get_all_book_copy_services():
    book_copies = BookCopies.query.all()
    if book_copies:
        return book_copies_schema.jsonify(book_copies)
    else:
        return jsonify({"message": "Not found book copy "}) , 404
    
def update_book_copy_by_id_services(id_copy):
    book_copy = BookCopies.query.get(id_copy)
    data = request.get_json()

    if not book_copy:
        return jsonify({"message": "Not found book copy"}), 404

    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        if "location" in data:
            book_copy.location = data["location"]

        if "status" in data:
            book_copy.status = data["status"]

        if "condition" in data:
            book_copy.condition = data["condition"]

        if "barcode" in data:
            book_copy.barcode = data["barcode"]

        if "qr_code" in data:
            book_copy.qr_code = data["qr_code"]

        if "received_date" in data:
            book_copy.received_date = datetime.strptime(
                data["received_date"], "%Y-%m-%d"
            ).date()

        if "id_book" in data:
            book_copy.id_book = data["id_book"]

        db.session.commit()
        return jsonify(book_copy_schema.dump(book_copy)), 200

    except ValueError:
        db.session.rollback()
        return jsonify({"error": "received_date must be in format YYYY-MM-DD"}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        db.session.close()
        
def delete_book_copy_by_id_services(id_copy):
    book_copy = BookCopies.query.get(id_copy)
    if book_copy:
        try:
            db.session.delete(book_copy)
            db.session.commit()
            return "book copy deleted"
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "can not delete book copy "}) , 404
    else:
        return "Not found book copy"