from fastapi import FastAPI
import psycopg2
import uvicorn

app = FastAPI()

# Connect to the database
conn = psycopg2.connect(r"postgresql://ronald:wZ6PuHWFiPFloIyAC-73ng@brass-pelican-10160.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=/Users/ron/Documents/cluster/BitCamp2023/root.crt")

# Create a cursor object
cur = conn.cursor()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/create_table/")
async def create_table(table_name: str):
    # Create a table
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL
        )
    """)

    # Commit the changes
    conn.commit()
    return {"message": f"Table '{table_name}' created successfully"}

@app.post("/insert_row/")
async def insert_row(table_name: str, name: str, age: int):
    # Insert a new row
    cur.execute(f"""
        INSERT INTO {table_name} (name, age)
        VALUES (%s, %s)
    """, (name, age))

    # Commit the changes
    conn.commit()

    return {"message": "Row inserted successfully"}

@app.put("/edit_row/")
async def edit_row(table_name: str, row_id: int, name: str, age: int):
    # Update a row
    cur.execute(f"""
        UPDATE {table_name}
        SET name = %s, age = %s
        WHERE id = %s
    """, (name, age, row_id))

    # Commit the changes
    conn.commit()

    return {"message": f"Row {row_id} updated successfully"}

@app.get("/get_rows/")
async def get_rows(table_name: str):
    # Select all rows from the table
    cur.execute(f"""
        SELECT * FROM {table_name}
    """)

    # Fetch all the results as a list of dictionaries
    rows = cur.fetchall()
    results = []
    for row in rows:
        results.append({"id": row[0], "name": row[1], "age": row[2]})

    return {"rows": results}


@app.delete("/delete_row/")
async def delete_row(table_name: str, row_id: int):
    # Delete a row
    cur.execute(f"""
        DELETE FROM {table_name}
        WHERE id = %s
    """, (row_id,))

    # Commit the changes
    conn.commit()

    return {"message": f"Row {row_id} deleted successfully"}


# Close the cursor and connection when the app stops
@app.on_event("shutdown")
async def shutdown_event():
    cur.close()
    conn.close()


# Run the app with `uvicorn app:app --reload`
if __name__ == "__main__":
    uvicorn.run(app, host="121.0.0.1", port=8000)
