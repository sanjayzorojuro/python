'''import mysql.connector

# Step 1: Connect to MySQL Server
con = mysql.connector.connect(
 host="localhost",
 user="root",
 password="" # Replace with your password if needed
)


cursor = con.cursor()
# Step 2: Create and Use Database
cursor.execute("CREATE DATABASE IF NOT EXISTS employeedb")
con.database = "employeedb"
# Step 3: Create Employee Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
 empno INT PRIMARY KEY,
 name VARCHAR(100),
 salary FLOAT
)
""")


# Step 4: Menu-driven operations
while True:
    print("\n===== Employee Database Menu =====")
    print("1. Add New Employee")
    print("2. View Specific Employee by Emp No")
    print("3. View Employees by Salary Range")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
if choice == '1':
    try:
        empno = int(input("Enter Employee Number: "))
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))
        sql = "INSERT INTO employee (empno, name, salary) VALUES (%s, %s, %s)"
        values = (empno, name, salary)
        cursor.execute(sql, values)
        con.commit()
        print("Employee added successfully.")
    except mysql.connector.IntegrityError:
         print("Error: Emp No already exists.")
    except ValueError:
        print("Invalid input. Try again.")
elif choice == '2':
    try:
        empno = int(input("Enter Employee Number: "))
        cursor.execute("SELECT * FROM employee WHERE empno = %s", (empno,))
        record = cursor.fetchone()
        if record:
            print(f"Emp No: {record[0]}, Name: {record[1]}, Salary: {record[2]}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input.")

elif choice == '3':
    try:
        min_salary = float(input("Enter Minimum Salary: "))
        max_salary = float(input("Enter Maximum Salary: "))
        cursor.execute("SELECT * FROM employee WHERE salary BETWEEN %s AND %s",(min_salary, max_salary))
        records = cursor.fetchall()
        if records:
            print("\nEmployees in Salary Range:")
            for row in records:
                print(f"Emp No: {row[0]}, Name: {row[1]}, Salary: {row[2]}")
        else:
                print("No employees found in that range.")
    except ValueError:
        print("Invalid input.")
elif choice == '4':
    print("Exiting program...")
    # break
else:
    print("Invalid choice. Please choose 1 to 4.")


# Step 5: Close Connection
cursor.close()
con.close()'''