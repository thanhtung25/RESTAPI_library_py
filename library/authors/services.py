from flask import request, jsonify
from library.extension import db
from library.library_ma import AuthorsSchema
from library.model import Authors

author_schema = AuthorsSchema()
authors_schema = AuthorsSchema(many=True)


def add_author_service():
    data = request.get_json()
    if not data or "full_name" not in data:
        return jsonify({"error": "full_name is required"}), 400

    try:
        new_author = Authors(
            full_name=data["full_name"],
            biography=data.get("biography")
        )
        db.session.add(new_author)
        db.session.commit()
        return jsonify(author_schema.dump(new_author)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def get_all_author_services():
    authors = Authors.query.all()
    return jsonify(authors_schema.dump(authors)), 200


def get_author_by_id_services(id_author):
    author = Authors.query.get(id_author)
    if not author:
        return jsonify({"message": "Not found author"}), 404
    return jsonify(author_schema.dump(author)), 200


def update_author_by_id_services(id_author):
    author = Authors.query.get(id_author)
    data = request.get_json()

    if not author:
        return jsonify({"message": "Not found author"}), 404
    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        if "full_name" in data:
            author.full_name = data["full_name"]
        if "biography" in data:
            author.biography = data["biography"]

        db.session.commit()
        return jsonify(author_schema.dump(author)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def delete_author_by_id_services(id_author):
    author = Authors.query.get(id_author)
    if not author:
        return jsonify({"message": "Not found author"}), 404

    try:
        db.session.delete(author)
        db.session.commit()
        return jsonify({"message": "Author deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()