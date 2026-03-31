from flask import Blueprint
from .services import (add_book_service, get_book_by_id_services
                    ,get_all_book_services,update_book_by_id_services,
                    delete_book_by_id_services,
                    get_book_by_category_service,
                    upload_book_image_service)
books = Blueprint("book", __name__)



#get all book
@books.route("/book-management/books", methods= ['GET'])
def get_all_book():
    return get_all_book_services()

#add book
@books.route("/book-management/book", methods= ['POST'] )
def add_book():
    return add_book_service()

#get book by id
@books.route("/book-management/book/<int:id_book>", methods= ['GET'] )
def get_book_id(id_book):
    return get_book_by_id_services(id_book)

# update book
@books.route("/book-management/book/<int:id_book>", methods= ['PUT'] )
def update_book_id(id_book):
    return update_book_by_id_services(id_book)

# delete book
@books.route("/book-management/book/<int:id_book>", methods= ['DELETE'] )
def delete_book_id(id_book):
    return delete_book_by_id_services(id_book)

# get book by category
@books.route("/book-management/book/<string:category>", methods= ['GET'] )
def get_book_by_category(category):
    return get_book_by_category_service(category)

@books.route("/book-management/book/<int:id_book>/image_book", methods=['PUT'])
def upload_book_image(id_book):
    return upload_book_image_service(id_book)