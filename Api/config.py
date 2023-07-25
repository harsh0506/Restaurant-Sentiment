import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Replace 'your_database_uri' with the connection URI to your PostgreSQL database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False