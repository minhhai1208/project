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
sql_query = "SELECT * FROM departments ;"


# Execute the SQL query
cur.execute(sql_query)

# Fetch all the results
tables = cur.fetchall()

print(tables)
# Print the result
for table in tables:
    print(table)
print("hello")
# Close the cursor and connection
cur.close()
conn.close()
