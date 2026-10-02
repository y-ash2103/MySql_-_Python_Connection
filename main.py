from dotenv import load_dotenv
import os
import dotenv
import mysql.connector

load_dotenv()

host=os.getenv("DB_HOST")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
db_name=os.getenv("DB_NAME")

try:
    conn=mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    print("Database connected successfully")
except Exception as e:
    print(f"Database connection failed: {e}")

def create_table():
    try:
        conn=mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        cursor=conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
        conn.commit()
        print("Table created successfully")
    except Exception as e:
        print(f"Table creation failed: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Database connection closed")

def insert_data():
    try:
        conn=mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        cursor=conn.cursor()
        cursor.execute("INSERT INTO test (name, age) VALUES ('John', 25)")
        conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print(f"Data insertion failed: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Database connection closed")

def fetch_data():
    try:
        conn=mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM test")
        rows=cursor.fetchall()
        print("Data fetched successfully")
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Data fetching failed: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Database connection closed")

if __name__ == "__main__":
    create_table()
    insert_data()
    fetch_data()