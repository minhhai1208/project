import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="itversity_retail_db",
    user="postgres",
    password="Yandere128@",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Write your SQL query
sql_query = "SELECT * FROM departments ;g"


# Execute the SQL query
cur.execute(sql_query)

# Fetch all the results
tables = cur.fetchall()

print(tables)
# Print the result
for table in tables:
    print(table)
<<<<<<< HEAD

=======
print("hello")
print("in cho vui")
>>>>>>> 2521d09a3d11080c07a11dcd2360adc21a2508eb
# Close the cursor and connection
cur.close()
conn.close()
