import psycopg2.extras
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("DB_HOST"))
print(os.getenv("DB_PORT"))
print(os.getenv("DB_NAME"))
print(os.getenv("DB_USER"))
print(os.getenv("DB_PASSWORD"))

def get_connection():
    return psycopg2.connect(
            host= os.getenv("DB_HOST"),
            port= os.getenv("DB_PORT"),
            dbname= os.getenv("DB_NAME"),
            user= os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"))