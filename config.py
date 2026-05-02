import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, os.getenv("MODEL_PATH"))

DATABASE_URL = os.getenv("DATABASE_URL")