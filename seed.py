from app import create_app
from library.data import seed_basic_library_data

app = create_app()

with app.app_context():
    seed_basic_library_data()