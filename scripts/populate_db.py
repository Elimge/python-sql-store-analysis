# scripts/populate_db.py

from faker import Faker
from faker_commerce import Provider
import random
# Import the custom database connector function
from utils.db_connector import get_db_connection

# --- Data Generation Configuration ---
NUM_CUSTOMERS = 50
NUM_PRODUCTS = 20
NUM_SALES = 200

# Initialize Fake instance 
fake = Faker()

# Personalized list to generate product names
PRODUCT_DESCRIPTORS = [
    "Ergonomic", "Wireless", "Mechanical", "Smart", "HD", "4K", "Portable",
    "Compact", "Gaming", "Premium", "Bluetooth", "Lightweight", "Waterproof"
]
PRODUCT_NOUNS = [
    "Keyboard", "Mouse", "Monitor", "Headphones", "Webcam", "Desk Chair",
    "USB Hub", "Laptop Stand", "Coffee Mug", "Smartwatch", "Speaker", "Mic"
]
# --------------------------------------------------------------------

def populate_customers(conn):
    """Populates the customers table with fake data."""
    with conn.cursor() as cur:
        print("Populating customers table...")
        for _ in range(NUM_CUSTOMERS):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.unique.email()
            cur.execute(
                "INSERT INTO customers (first_name, last_name, email) VALUES (%s, %s, %s)",
                (first_name, last_name, email)
            )
    print("Customers table populated")

def populate_products(conn):
    """Populates the products table with fake data."""
    with conn.cursor() as cur:
        print("Populating products table...")
        generated_products = set()

        while len(generated_products) < NUM_PRODUCTS:
            descriptor = random.choice(PRODUCT_DESCRIPTORS)
            noun = random.choice(PRODUCT_NOUNS)
            product_name = f"{descriptor} {noun}"

            # Don't generate the same product twice
            if product_name not in generated_products:
                generated_products.add(product_name)
                
                price = round(random.uniform(15.0, 350.0), 2)
                cur.execute(
                    "INSERT INTO products (product_name, price) VALUES (%s, %s)",
                    (product_name, price)
                )
    print("Products table populated.")

def populate_sales(conn):
    """Populates the sales table with fake data, linking customers and products."""
    with conn.cursor() as cur:
        print("Fetching existing customer and product IDs...")
        cur.execute("SELECT customer_id FROM customers")
        customer_ids = [row[0] for row in cur.fetchall()]
        cur.execute("SELECT product_id FROM products")
        product_ids = [row[0] for row in cur.fetchall()]
        if not customer_ids or not product_ids:
            print("Cannot populate sales. Customers or products table is empty.")
            return
        
        print("Populating sales table...")
        for _ in range(NUM_SALES):
            customer_id = random.choice(customer_ids)
            product_id = random.choice(product_ids)
            quantity = random.randint(1, 5)
            sale_date = fake.date_time_between(start_date="-2y", end_date="now")
            cur.execute(
                "INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES (%s, %s, %s, %s)",
                (customer_id, product_id, quantity, sale_date)          
            )  
    print("Sales table populated.")
            
def main():
    """Main function to connect to the DB and populate all tables."""
    conn = get_db_connection()

    # If connection fails, the function returns None and stop execution.
    if not conn:
        return
    
    try:
        # Before populating, clean the tables
        # to avoid duplicating data on successive runs.
        with conn.cursor() as cur:
            print("Cleaning old data...")
            cur.execute("TRUNCATE TABLE sales, customers, products RESTART IDENTITY CASCADE;")

        #populates tables
        populate_customers(conn)
        populate_products(conn)
        populate_sales(conn)

        # Commit all changes
        conn.commit()
        print("\nAll data committed successfully")

    except Exception as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.rollback()
            print("Transaction rolled back.")
    
    finally:
        #Ensure the connection is closed
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
