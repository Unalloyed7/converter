import os
from dotenv import load_dotenv
load_dotenv()

CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
DATABASE_URL = os.getenv("DATABASE_URL")
 