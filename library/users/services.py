from datetime import datetime
from flask import request, jsonify
from library.extension import db
from library.library_ma import UsersSchema
from library.model import Users

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)


def add_user_service():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400

    required_fields = ["full_name", "username", "password", "role"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    try:
        username = data["username"].strip()

        # kiểm tra username đã tồn tại chưa
        existing_user = Users.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"error": "Username already exists"}), 400
        
        birth_day = None
        if data.get("birth_day"):
            birth_day = datetime.strptime(data["birth_day"], "%Y-%m-%d").date()

        new_user = Users(
            full_name=data["full_name"],
            birth_day=birth_day,
            gender=data.get("gender"),
            email=data.get("email"),
            phone=data.get("phone"),
            username=data["username"],
            password=data["password"],
            role=data["role"],
            status=data.get("status", "active"),
            created_at=datetime.utcnow(),
            library_card=data.get("library_card"),
            address=data.get("address"),
            avatar_url=data.get("avatar_url")
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(user_schema.dump(new_user)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def get_all_user_services():
    users = Users.query.all()
    return jsonify(users_schema.dump(users)), 200


def get_user_by_id_services(id_user):
    user = Users.query.get(id_user)
    if not user:
        return jsonify({"message": "Not found user"}), 404
    return jsonify(user_schema.dump(user)), 200


def update_user_by_id_services(id_user):
    user = Users.query.get(id_user)
    data = request.get_json()

    if not user:
        return jsonify({"message": "Not found user"}), 404
    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        for field in [
            "full_name", "gender", "email", "phone", "username", "password",
            "role", "status", "library_card", "address", "avatar_url"
        ]:
            if field in data:
                setattr(user, field, data[field])

        if "birth_day" in data:
            user.birth_day = datetime.strptime(data["birth_day"], "%Y-%m-%d").date()

        db.session.commit()
        return jsonify(user_schema.dump(user)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def delete_user_by_id_services(id_user):
    user = Users.query.get(id_user)
    if not user:
        return jsonify({"message": "Not found user"}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def login_services():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400

    try:
        user = Users.query.filter_by(username=username).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        if user.password != password:
            return jsonify({"error": "Wrong password"}), 401

        if user.status != "active":
            return jsonify({"error": "User inactive"}), 403

        return jsonify({
            "message": "Login success",
            "user": user_schema.dump(user)
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500