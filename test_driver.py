# import psycopg2
#
# # Connect to the database
# conn = psycopg2.connect(r"postgresql://ronald:wZ6PuHWFiPFloIyAC-73ng@brass-pelican-10160.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=C:\Users\He\Downloads\hoohack2023-main\BitCamp2023\root.crt")
#
# # Create a cursor object
# cur = conn.cursor()
#
# # Execute a SELECT query against the pg_catalog.pg_tables table
# cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';")
#
# # Fetch all the results as a list of tuples
# rows = cur.fetchall()
#
# # Print the table names
# for row in rows:
#     print(row[0])
#
# # Close the cursor and connection
# cur.close()
# conn.close()
# print('1'*200)
#
# import httpx
# import random
# import string
#
# # Generate a random username, password, security question, and response
# username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
# password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
# security_question = 'What is your favorite color?'
# response = 'blue'
#
# # Make a POST request to the signup endpoint with the random user information
# response = httpx.post('http://localhost:8000/signup/', json={
#         'username': username,
#     'password': password,
#     'security_question': security_question,
#     'response': response
# })
#
# # Check the response status code
# if response.status_code == 200:
#     print('User successfully created')
# else:
#     print('Error creating user:', response.text)

# Example driver
# import requests
# import json
#
# # Define the base URL for the API
# BASE_URL = "http://localhost:8000"
#
# # Define the data to be sent in the request body
# data = {"param": "test"}
# json_data = json.dumps(data)  # Convert data to JSON
#
# # Make a test POST request with a parameter
# response = requests.post(f"{BASE_URL}/test/", data=json_data)
# print(response.json())  # should print: {"message": "Received parameter: test"}
#




import requests

# Define the base URL for the API
BASE_URL = "http://localhost:8000"

# Define the parameters for the new user
username = "testuser"
password = "testpassword"
security_question = "What is your favorite color?"
response = "Blue"

# Send a POST request to create the new user
response = requests.post(f"{BASE_URL}/signup/", json={
    "username": username,
    "password": password,
    "security_question": security_question,
    "response": response
})

# Check the response from the server
if response.status_code == 200:
    print("User created successfully")
else:
    print(f"Error creating user: {response.json()}")
