#import os
#from dotenv import load_dotenv

#load_dotenv()
#SECRET_KEY = os.environ.get("KEY")
#SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
#SQLALCHEMY_TRACK_MODIFICATIONS = False

import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("KEY", "library_api")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///library.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False