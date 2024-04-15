import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class ProdConfig():
    DEBUG = False
    SQLITE_DB_DIR = os.path.join(base_dir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(SQLITE_DB_DIR, "studentdb.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DebugConfig():
    DEBUG = True
    SQLITE_DB_DIR = os.path.join(base_dir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(SQLITE_DB_DIR, "studentdb.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
