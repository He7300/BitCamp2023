import psycopg2

# Connect to the database
conn = psycopg2.connect(r"postgresql://ronald:wZ6PuHWFiPFloIyAC-73ng@brass-pelican-10160.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=C:\Users\He\Downloads\hoohack2023-main\BitCamp2023\root.crt")

# Create a cursor object
cur = conn.cursor()

# Execute a SELECT query against the pg_catalog.pg_tables table
cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';")

# Fetch all the results as a list of tuples
rows = cur.fetchall()

# Print the table names
for row in rows:
    print(row[0])

# Close the cursor and connection
cur.close()
conn.close()
print('1'*200)

