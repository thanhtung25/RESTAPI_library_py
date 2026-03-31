import os
import uuid
from library.extension import db
from library.library_ma import BooksSchema
from library.model import Books , Categories
from flask import request, jsonify, current_app
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename



book_schema = BooksSchema()
books_schema = BooksSchema(many=True)

_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def add_book_service():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400
    required_fields = [
        "title",
        "isbn",
        "language",
        "publish_year",
        "description",
        "image_url",
        "id_category",
        "id_author"
    ]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400
    try:
        new_book = Books(
            data["id_category"],
            data["id_author"],
            data["title"],
            data["isbn"],
            data["language"],
            data["publish_year"],
            data["description"],
            data["image_url"]
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify(book_schema.dump(new_book)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": str(e)
        }), 500
    

def get_book_by_id_services(id_book):
    book = Books.query.get(id_book)
    if book:
        return book_schema.jsonify(book)
    else:
        return jsonify({"message": "Not found books "}) , 404

def get_all_book_services():
    books = Books.query.all()
    if books:
        return books_schema.jsonify(books)
    else:
        return jsonify({"message": "Not found books "}) , 404
    
def update_book_by_id_services(id_book):
    book = Books.query.get(id_book)
    data = request.get_json()

    if not book:
        return jsonify({"message": "Not found book"}), 404

    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        if "title" in data:
            book.title = data["title"]

        if "isbn" in data:
            book.isbn = data["isbn"]

        if "language" in data:
            book.language = data["language"]

        if "publish_year" in data:
            book.publish_year = data["publish_year"]

        if "description" in data:
            book.description = data["description"]

        if "image_url" in data:
            book.image_url = data["image_url"]

        if "id_category" in data:
            book.id_category = data["id_category"]

        if "id_author" in data:
            book.id_author = data["id_author"]

        db.session.commit()

        return jsonify(book_schema.dump(book)), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "can not update book", "error": str(e)}), 500

    finally:
        db.session.close()
        
def delete_book_by_id_services(id_book):
    book = Books.query.get(id_book)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return "book deleted"
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "can not delete book "}) , 404
    else:
        return "Not found book"
    

def get_book_by_category_service(category):
    category = category.strip()

    books = (
        Books.query
        .join(Categories)
        .filter(Categories.name == category)
        .all()
    )

    if books:
        return books_schema.jsonify(books)
    else:
        return jsonify({"message": f"Not found books by {category}"}), 404
    
    
def _allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in _ALLOWED_EXTENSIONS


def upload_book_image_service(id_book):
    book = Books.query.get(id_book)
    if not book:
        return jsonify({"message": "Not found book"}), 404
    if "books" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["books"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400
    if not _allowed_file(file.filename):
        return jsonify({"error": "Invalid image format"}), 400
    try:
        filename = secure_filename(file.filename)
        ext = filename.rsplit(".", 1)[1].lower()
        new_filename = f"{uuid.uuid4().hex}.{ext}"
        upload_folder = os.path.join(
                current_app.root_path,
                "static",
                "uploads",
                "books"
            )
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, new_filename)
        file.save(file_path)

        book.image_url = f"/static/uploads/books/{new_filename}"
        db.session.commit()

        return jsonify({
            "message": "Book uploaded successfully",
            "image_url": book.image_url,
            "book": book_schema.dump(book)
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()

