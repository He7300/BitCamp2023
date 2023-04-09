import hashlib
import bcrypt
from fastapi import FastAPI
import psycopg2
import uvicorn
from pydantic import BaseModel

app = FastAPI()

# Connect to the database
conn = psycopg2.connect(
    r"postgresql://ronald:wZ6PuHWFiPFloIyAC-73ng@brass-pelican-10160.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=C:\Users\He\Downloads\hoohack2023-main\BitCamp2023\root.crt")

# Create a cursor object
cur = conn.cursor()
SECRET_KEY = 'My-New-Key'

class User(BaseModel):
    username: str
    password: str
    security_question: str
    response: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/signup/")
async def signup(User):
    # Hash the password using a secure algorithm
    hashed_password = bcrypt.hashpw(User.password.encode('utf-8'), bcrypt.gensalt())

    # Insert the new user into the database
    cur.execute("""
        INSERT INTO users (username, password, security_question, response)
        VALUES (%s, %s, %s, %s)
    """, (User.username, hashed_password, User.security_question, User.response))

    # Commit the changes

    conn.commit()

    return {"message": "user successfully created"}


@app.post("/login/")
async def login(username: str, password: str, jwt=None):
    # Hash the password to compare it to the stored hash
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the user exists and the password is correct
    cur.execute(f"""
        SELECT id FROM users
        WHERE username = %s AND password = %s
    """, (username, hashed_password))
    user_id = cur.fetchone()

    if user_id:
        # Generate a JWT token with the user ID as the payload
        token = jwt.encode({"user_id": user_id[0]}, SECRET_KEY)

        # Return the token
        return {"token": token}

    # If the credentials are invalid, return an error message
    return {"message": "Invalid username or password"}

# Example test post function
@app.post("/test/")
async def test_post(param: str):
    print(param)
    return {"message": f"Received parameter: {param}"}


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


@app.get("/get_all_rows/")
async def get_all_rows():
    # Get all table names
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
        AND table_type='BASE TABLE'
    """)
    table_names = [name[0] for name in cur.fetchall()]

    # Fetch all rows from all tables
    results = {}
    for table_name in table_names:
        cur.execute(f"""
            SELECT * FROM {table_name}
        """)
        rows = cur.fetchall()
        table_results = []
        for row in rows:
            table_results.append({"id": row[0], "name": row[1], "age": row[2]})
        results[table_name] = table_results

    return {"tables": results}


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
    uvicorn.run(app, host="0.0.0.0", port=8000)
