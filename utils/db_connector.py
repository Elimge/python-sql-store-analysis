# utils/db_connector.py

import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from the .env file in the project root
load_dotenv()

def get_db_connection():
    """
    Establishes and returns a connection to the PostgreSQL database.
    Handles connection errors gracefully.
    
    Returns:
        psycopg2.connection or None: A connection object if successful, None otherwise.
    """
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("Database connection successful.")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None