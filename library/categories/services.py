from flask import request, jsonify
from library.extension import db
from library.library_ma import CategoriesSchema
from library.model import Categories

category_schema = CategoriesSchema()
categories_schema = CategoriesSchema(many=True)


def add_category_service():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "name is required"}), 400

    try:
        new_category = Categories(
            name=data["name"],
            description=data.get("description")
        )
        db.session.add(new_category)
        db.session.commit()
        return jsonify(category_schema.dump(new_category)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def get_all_category_services():
    categories = Categories.query.all()
    return jsonify(categories_schema.dump(categories)), 200


def get_category_by_id_services(id_category):
    category = Categories.query.get(id_category)
    if not category:
        return jsonify({"message": "Not found category"}), 404
    return jsonify(category_schema.dump(category)), 200


def update_category_by_id_services(id_category):
    category = Categories.query.get(id_category)
    data = request.get_json()

    if not category:
        return jsonify({"message": "Not found category"}), 404
    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        if "name" in data:
            category.name = data["name"]
        if "description" in data:
            category.description = data["description"]

        db.session.commit()
        return jsonify(category_schema.dump(category)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def delete_category_by_id_services(id_category):
    category = Categories.query.get(id_category)
    if not category:
        return jsonify({"message": "Not found category"}), 404

    try:
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": "Category deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()