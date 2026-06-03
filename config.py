from dotenv import load_dotenv
import os

load_dotenv()

APIFY_TOKEN = os.getenv("APIFY_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")