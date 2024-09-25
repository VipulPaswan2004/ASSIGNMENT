import pandas as pd
import mysql.connector  # MySQL connector to connect to the database

# Step 1: Establish the MySQL connection with correct username and password
conn = mysql.connector.connect(
    host='localhost',    # MySQL server host
    user='root',         # Replace with your MySQL username (e.g., 'root')
    password='Vipul@123456789',  # Replace with your MySQL password
    database='Travel_planner'  # Connect to the Travel_planner database
)

# Step 2: Write the SQL query to read the bookings table
query = "SELECT * FROM bookings;"

# Step 3: Use pandas to execute the query and fetch the data into a DataFrame
df = pd.read_sql(query, conn)

# Step 4: Display the DataFrame to show the contents of the bookings table
print(df)

# Step 5: Close the connection
conn.close()
