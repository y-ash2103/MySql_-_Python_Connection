# 🐍 Python + MySQL Student Database

A beginner-friendly project demonstrating how to connect **Python with MySQL**, create and manage a student database, insert records, retrieve data, and display the results using Pandas.

The project uses a MySQL database named **`TPS`** with a `students` table.

---

## 📌 Project Overview

This project demonstrates:

* Connecting Python to MySQL
* Creating a MySQL database and table
* Inserting student records
* Reading student records
* Displaying column names
* Using Python for SQL queries
* Using Pandas to display database data
* Storing database credentials securely with `.env`

---

## 🛠️ Technologies Used

| Technology             | Purpose                             |
| ---------------------- | ----------------------------------- |
| Python                 | Application programming             |
| MySQL                  | Database                            |
| mysql-connector-python | Python ↔ MySQL connection           |
| python-dotenv          | Environment variables               |
| Pandas                 | Data analysis and DataFrame display |

---

# 📂 Project Structure

```text
Python-MySQL-Connection/
│
├── app.py                 # Main Python application
├── database.py            # MySQL connection configuration
├── students.sql           # Database/table/sample data
├── requirements.txt       # Python dependencies
├── .env                   # Database credentials (do not commit)
├── .gitignore             # Files ignored by Git
└── README.md              # Project documentation
```

### File Responsibilities

**`database.py`**

Responsible only for creating the MySQL connection.

**`app.py`**

Responsible for:

* Reading students
* Displaying column names
* Inserting students
* Running SQL queries
* Closing the database connection

**`students.sql`**

Contains the SQL required to create the `TPS` database, `students` table, and sample records.

**`.env`**

Stores MySQL credentials.

---

# 🗄️ Database Structure

```text
TPS
└── students
    ├── student_id
    ├── name
    ├── age
    ├── gender
    ├── course
    ├── email
    ├── phone
    ├── city
    ├── marks
    └── admission_year
```

### Students Table

| Column           | Type         | Description       |
| ---------------- | ------------ | ----------------- |
| `student_id`     | INT          | Unique student ID |
| `name`           | VARCHAR(100) | Student name      |
| `age`            | INT          | Student age       |
| `gender`         | VARCHAR(10)  | Student gender    |
| `course`         | VARCHAR(100) | Course name       |
| `email`          | VARCHAR(100) | Email address     |
| `phone`          | VARCHAR(15)  | Phone number      |
| `city`           | VARCHAR(50)  | City              |
| `marks`          | DECIMAL(5,2) | Student marks     |
| `admission_year` | YEAR         | Admission year    |

---

# ⚙️ Installation

## 1. Clone or Download the Project

```bash
git clone https://github.com/y-ash2103/MySql_-_Python_Connection
cd Python-MySQL-Connection
```

Or simply open the project folder if you already have it.

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
mysql-connector-python
python-dotenv
pandas
```

---

# 🗄️ 4. Setup MySQL

Open **MySQL Workbench** or the MySQL terminal.

You can run the complete `students.sql` file.

The important database commands are:

```sql
CREATE DATABASE TPS;

USE TPS;

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(10),
    course VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    city VARCHAR(50),
    marks DECIMAL(5,2),
    admission_year YEAR
);
```

The `students.sql` file should also contain the sample student records.

---

# 🔐 5. Configure `.env`

Create a file named:

```text
.env
```

Add:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=TPS
```

For example:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=1234
DB_NAME=TPS
```

> ⚠️ Do not upload `.env` to GitHub. It contains your database password.

---

# 🔌 6. `database.py`

The connection logic is kept separately in `database.py`.

```python
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection
```

This file contains **only the database connection function**.

---

# 🐍 7. `app.py`

The main application uses the connection from `database.py`.

```python
from database import get_connection
import pandas as pd


def read_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    # Get column names
    columns = [column[0] for column in cursor.description]

    students = cursor.fetchall()

    print("\nColumns:")
    print(columns)

    print("\nStudents:")
    for student in students:
        print(student)

    cursor.close()
    connection.close()


def insert_student():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO students
    (name, age, gender, course, email, phone, city, marks, admission_year)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        "Yash Sharma",
        21,
        "Male",
        "B.Tech Computer Science",
        "yash@gmail.com",
        "9876543220",
        "Bhopal",
        90.50,
        2024
    )

    cursor.execute(query, values)

    connection.commit()

    print("\nStudent inserted successfully!")

    cursor.close()
    connection.close()


def display_with_pandas():
    connection = get_connection()

    query = "SELECT * FROM students"

    df = pd.read_sql(query, connection)

    print("\nStudent Data:")
    print(df)

    connection.close()


if __name__ == "__main__":

    print("1. Read students")
    print("2. Insert student")
    print("3. Display using Pandas")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        read_students()

    elif choice == "2":
        insert_student()

    elif choice == "3":
        display_with_pandas()

    else:
        print("Invalid choice")
```

---

# ▶️ 8. Run the Application

From the project directory:

```bash
python app.py
```

You will see:

```text
1. Read students
2. Insert student
3. Display using Pandas

Enter your choice:
```

### Option 1 — Read Students

Enter:

```text
1
```

Output:

```text
Columns:
['student_id', 'name', 'age', 'gender', 'course',
 'email', 'phone', 'city', 'marks', 'admission_year']

Students:
(1, 'Aarav Sharma', 21, 'Male', ...)
(2, 'Priya Verma', 20, 'Female', ...)
...
```

### Option 2 — Insert Student

Enter:

```text
2
```

The application inserts the predefined student:

```text
Yash Sharma
```

and commits it to MySQL.

### Option 3 — Pandas

Enter:

```text
3
```

The students table is loaded into a Pandas DataFrame.

---

# ➕ Insert Data Directly with SQL

You can also insert records from MySQL:

```sql
INSERT INTO students
(name, age, gender, course, email, phone, city, marks, admission_year)
VALUES
(
    'Yash Sharma',
    21,
    'Male',
    'B.Tech Computer Science',
    'yash@gmail.com',
    '9876543220',
    'Bhopal',
    90.50,
    2024
);
```

---

# 🔎 Useful SQL Queries

### Get all students

```sql
SELECT * FROM students;
```

### Students with marks above 85

```sql
SELECT *
FROM students
WHERE marks > 85;
```

### Students from Bhopal

```sql
SELECT *
FROM students
WHERE city = 'Bhopal';
```

### Highest-scoring student

```sql
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 1;
```

### Average marks

```sql
SELECT AVG(marks) AS average_marks
FROM students;
```

### Count students

```sql
SELECT COUNT(*) AS total_students
FROM students;
```

---

# 📊 Pandas DataFrame

The project can load the SQL table into Pandas:

```python
query = "SELECT * FROM students"

df = pd.read_sql(query, connection)

print(df)
```

This makes the data available for:

* Data Analysis
* EDA
* Visualization
* Machine Learning
* Data preprocessing

---

# 📦 requirements.txt

```text
mysql-connector-python
python-dotenv
pandas
```

Install them with:

```bash
pip install -r requirements.txt
```

---

# 🚫 .gitignore

```text
.env
venv/
.venv/
__pycache__/
*.pyc
```

This keeps credentials, virtual environments, and Python cache files out of Git.

---

# 🔄 Application Flow

```text
                    app.py
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
      Read Data    Insert Data   Pandas
          │           │           │
          └───────────┼───────────┘
                      ▼
                 database.py
                      │
                      ▼
              get_connection()
                      │
                      ▼
                 .env
                      │
                      ▼
                MySQL Server
                      │
                      ▼
                  Database
                    TPS
                      │
                      ▼
                 students
```

---

# 🎯 Learning Objectives

After completing this project, you will understand:

* How Python connects to MySQL
* How to separate database logic from application logic
* How to use `.env` for credentials
* How to execute SQL queries from Python
* How to insert records using Python
* How to retrieve records using Python
* How to display column names
* How to use Pandas with MySQL
* Basic database operations

---

# 🚀 Future Improvements

This project can be extended with:

* Full CRUD operations
* Update student records
* Delete student records
* Search students
* User input for inserting students
* Flask web application
* Streamlit dashboard
* REST API
* Authentication
* SQLAlchemy
* Student analytics
* Machine learning features

---

## 👨‍💻 Author

**Yash**

Python | Machine Learning | Data Science | Generative AI
