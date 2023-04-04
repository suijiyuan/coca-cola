import secrets

DEBUG = False
SECRET_KEY = secrets.token_hex(16)
DATABASE_URI = 'sqlite:///my_database.db'
