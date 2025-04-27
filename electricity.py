'''import mysql.connector
# Connect to MySQL Server
con = mysql.connector.connect(
 host="localhost",
 user="root",
 password=""
)
cursor = con.cursor()
# Create and use the database
cursor.execute("CREATE DATABASE IF NOT EXISTS electricitydb")
con.database = "electricitydb"
# Create electricity_bill table
cursor.execute("""
CREATE TABLE IF NOT EXISTS electricity_bill (
 TariffCode VARCHAR(10),
 Customer_Name VARCHAR(100),
 Meter_Number INT PRIMARY KEY,
 Previous_Reading INT,
 Current_Reading INT
)
""")
# Function to calculate bill based on units and tariff code
def calculate_bill(units, tariff):
 bill = 0
 if tariff == 'LT1':
 if units <= 30:
 bill += units * 2.0
 elif units <= 100:
 bill += 30 * 2.0 + (units - 30) * 3.5
 elif units <= 200:
 bill += 30 * 2.0 + 70 * 3.5 + (units - 100) * 4.5
 else:
 bill += 30 * 2.0 + 70 * 3.5 + 100 * 4.5 + (units - 200) * 5.0
 elif tariff == 'LT2':
 if units <= 30:
 bill += units * 3.5
 elif units <= 100:
 bill += 30 * 3.5 + (units - 30) * 5.0
 elif units <= 200:
 bill += 30 * 3.5 + 70 * 5.0 + (units - 100) * 6.0
 else:
 bill += 30 * 3.5 + 70 * 5.0 + 100 * 6.0 + (units - 200) * 7.5
 return bill
# Menu
while True:
 print("\n===== Electricity Bill Menu =====")
 print("1. Add Customer Details")
 print("2. Update Customer by Meter Number")
 print("3. Calculate Bill for a Customer")
 print("4. Exit")
 ch = input("Enter your choice (1-4): ")
 if ch == '1':
 try:
 tariff = input("Enter Tariff Code (LT1/LT2): ").upper()
 name = input("Enter Customer Name: ")
 meter = int(input("Enter Meter Number: "))
 prev = int(input("Enter Previous Reading: "))
 curr = int(input("Enter Current Reading: "))
 sql = "INSERT INTO electricity_bill VALUES (%s, %s, %s, %s, %s)"
 values = (tariff, name, meter, prev, curr)
 cursor.execute(sql, values)
 con.commit()
 print("Customer added successfully.")
 except mysql.connector.IntegrityError:
 print("Meter Number already exists.")
 except:
 print("Error occurred. Please check input.")
 elif ch == '2':
 try:
 meter = int(input("Enter Meter Number to Update: "))
 name = input("Enter New Customer Name: ")
 prev = int(input("Enter New Previous Reading: "))
 curr = int(input("Enter New Current Reading: "))
 cursor.execute("UPDATE electricity_bill SET Customer_Name=%s,
Previous_Reading=%s, Current_Reading=%s WHERE Meter_Number=%s",
 (name, prev, curr, meter))
 con.commit()
 if cursor.rowcount > 0:
 print("Customer details updated.")
 else:
 print("Meter number not found.")
 except:
 print("Invalid input or error.")
 elif ch == '3':
 meter = int(input("Enter Meter Number to Calculate Bill: "))
 cursor.execute("SELECT * FROM electricity_bill WHERE Meter_Number = %s", (meter,))
 data = cursor.fetchone()
 if data:
 tariff, name, meter, prev, curr = data
 units = curr - prev
 if units < 0:
 print("Invalid readings. Current reading should be >= Previous.")
 else:
 bill = calculate_bill(units, tariff)
 print(f"\nCustomer: {name}")
 print(f"Tariff Code: {tariff}")
 print(f"Units Consumed: {units}")
 print(f"Total Bill: ₹{bill:.2f}")
 else:
 print("No customer found with this meter number.")
 elif ch == '4':
 print("Exiting...")
 break
 else:
 print("Invalid choice. Try again.")
# Close connection
cursor.close()
con.close()'''