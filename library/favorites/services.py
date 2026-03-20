from datetime import datetime
from flask import request, jsonify
from library.extension import db
from library.library_ma import FavoritesSchema
from library.model import Favorites

favorite_schema = FavoritesSchema()
favorites_schema = FavoritesSchema(many=True)


def add_favorite_service():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400
    if "id_user" not in data or "id_book" not in data:
        return jsonify({"error": "id_user and id_book are required"}), 400

    try:
        new_favorite = Favorites(
            id_user=data["id_user"],
            id_book=data["id_book"],
            created_at=datetime.utcnow()
        )
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify(favorite_schema.dump(new_favorite)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def get_all_favorite_services():
    favorites = Favorites.query.all()
    return jsonify(favorites_schema.dump(favorites)), 200


def get_favorite_by_id_services(id_favorite):
    favorite = Favorites.query.get(id_favorite)
    if not favorite:
        return jsonify({"message": "Not found favorite"}), 404
    return jsonify(favorite_schema.dump(favorite)), 200


def delete_favorite_by_id_services(id_favorite):
    favorite = Favorites.query.get(id_favorite)
    if not favorite:
        return jsonify({"message": "Not found favorite"}), 404

    try:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()