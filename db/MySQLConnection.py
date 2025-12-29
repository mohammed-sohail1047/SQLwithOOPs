# import mysql.connector as mysql

# DB_NAME = "Product_db"


# def MySQLConnection():
#     # Step 1: Connect to MySQL server (NO database yet)
#     connection = mysql.connect(
#         host="localhost",
#         user="root",
#         password="Sohail12"
#     )

#     cursor = connection.cursor()

#     try:
#         # Step 2: Create database
#         cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
#         print(f"✅ Database '{DB_NAME}' created or already exists")

#         # Step 3: Use database
#         cursor.execute(f"USE {DB_NAME}")

#         # Step 4: Create Department table
#         cursor.execute("""
#         CREATE TABLE IF NOT EXISTS Department (
#             DeptNo INT PRIMARY KEY,
#             Dname VARCHAR(30) UNIQUE NOT NULL,
#             Location VARCHAR(50)
#         )
#         """)
#         print("✅ Department table ready")

#         # Step 5: Create Employee table
#         cursor.execute("""
#         CREATE TABLE IF NOT EXISTS Employee (
#             EmpId INT PRIMARY KEY,
#             Ename VARCHAR(30),
#             Password VARCHAR(30),
#             Gender CHAR(10),
#             Dob DATE,
#             Phone VARCHAR(15),
#             Email VARCHAR(50),
#             Salary DECIMAL(10,2),
#             Address VARCHAR(100),
#             DeptNo INT,
#             FOREIGN KEY (DeptNo) REFERENCES Department(DeptNo)
#         )
#         """)
#         print("✅ Employee table ready")

#         connection.commit()

#     except Exception as e:
#         print("❌ Error during DB setup:", e)

#     finally:
#         cursor.close()
#         connection.close()
#         print("🔒 MySQL connection closed")


# if __name__ == "__main__":
#     MySQLConnection()


import mysql.connector as mysqlconn

class MySQLConnection:
    def __init__(self):
        self.connection = mysqlconn.connect(
            host='localhost',
            user='root',
            password='Sohail12',
            database= 'Product_db'
        )

    def get_connection(self):
        return self.connection


