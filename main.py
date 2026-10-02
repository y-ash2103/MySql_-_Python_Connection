import os
import dotenv
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("DB_HOST")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
db_name=os.getenv("DB_NAME")

#creating connection with database
def connect_to_mysql():
    try:
        conn=mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )   
        print("Database connected successfully")
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")

# creating table in the database
def create_table():
    try:
        conn=connect_to_mysql()

        cursor=conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

        conn.commit()
        print("\nTable created successfully")
    except Exception as e:
        print(f"Table creation failed: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("\nDatabase connection closed")

#incerting data into the table
def insert_data():
    try:
        conn=connect_to_mysql()
        
        cursor=conn.cursor()
        
        cursor.execute("INSERT INTO test (name, age) VALUES ('Yash', 22)")
        conn.commit()
        print("\nData inserted successfully")
    except Exception as e:
        print(f"\nData insertion failed: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("\nDatabase connection closed")

#fetching data from table
def fetch_data():
    try:
        conn=connect_to_mysql()

        cursor=conn.cursor()

        cursor.execute("SELECT * FROM test")
        rows=cursor.fetchall()
        print("\nData fetched successfully")
        for row in rows:
            print(row)
    except Exception as e:
        print(f"\nData fetching failed: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("\nDatabase connection closed")

# main function to run the program
if __name__ == "__main__":
    create_table()
    insert_data()
    fetch_data()