import os

SERVER = os.environ.get("SERVER", "http")
HOST = os.environ.get('HOST', "localhost")
PORT = os.environ.get("PORT", "8000")

ADDRESS = f'{SERVER}://{HOST}:{PORT}'
FILE_PATH = os.environ.get('FILE_PATH', './app/static/media')
