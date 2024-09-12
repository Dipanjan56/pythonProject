"""API BASICS"""

"""
### REST API Automation Basics with Path, Patch, and Other HTTP Methods

In this document, we will cover the fundamentals of REST API automation, including **path parameters** and the **PATCH** HTTP method, along with key concepts such as HTTP methods, headers, status codes, and how to automate them using Python.

---

### What is a REST API?

- **REST (Representational State Transfer)**: REST is an architectural style that defines a set of constraints to create 
web services. REST APIs use HTTP methods to interact with resources (data) on a server.
- **Client-Server Architecture**: The client sends requests to the server to access, create, update, or delete resources.
 Each resource is identified by a URL.

---

### Key Concepts of REST API:

#### 1. **HTTP Methods (Verbs)**
   REST APIs commonly use HTTP methods to perform CRUD operations:
   
   - **GET**: Retrieve data from the server. (Read)
   - **POST**: Send new data to the server to create a resource. (Create)
   - **PUT**: Update an existing resource entirely. (Update)
   - **PATCH**: Partially update an existing resource. (Partial Update)
   - **DELETE**: Delete a resource from the server. (Delete)
   
   **Examples**:
   ```
   GET /users            --> Retrieve all users
   POST /users           --> Create a new user
   PUT /users/123        --> Update user with ID 123
   PATCH /users/123      --> Partially update user with ID 123
   DELETE /users/123     --> Delete user with ID 123
   ```

---

#### 2. **Path Parameters**
   - **Path parameters** are used to identify specific resources. They are part of the URL path.
   - **Example**:
     ```
     GET /users/{user_id}
     ```
     The `{user_id}` is a path parameter. If you request `GET /users/123`, it retrieves the user with ID `123`.

---

#### 3. **Query Parameters**
   - **Query parameters** are appended to the end of the URL and are often used for filtering, sorting, or pagination. They follow the `?` and are separated by `&`.
   - **Example**:
     ```
     GET /users?age=25&city=NewYork
     ```
     This query fetches users who are 25 years old and live in New York.

---

#### 4. **Headers**
   - **Headers** provide metadata about the request or response. These are critical in sending authentication tokens, specifying content types, etc.
   - **Common Headers**:
     - **Authorization**: Contains the authentication token (e.g., Bearer token).
     - **Content-Type**: Indicates the format of the request body (e.g., `application/json`).
     - **Accept**: Specifies the response format expected by the client.
   
   **Example**:
   ```
   GET /users
   Headers:
   Authorization: Bearer {token}
   Content-Type: application/json
   ```

---

#### 5. **Request Body (Payload)**
   - The body contains the data you send to the server in **POST**, **PUT**, or **PATCH** requests. This data is usually in JSON format.
   - **Example (POST Request)**:
     ```json
     POST /users
     Body:
     {
       "name": "John Doe",
       "email": "john@example.com",
       "age": 25
     }
     ```

---

#### 6. **HTTP Status Codes**
   - **Status codes** indicate the result of an HTTP request. Some common codes include:
    •	200 OK: The request was successful.
	•	201 Created: The request was successful and a new resource was created.
	•	202 Accepted: The request has been accepted for processing but is not yet complete.
	•	204 No Content: The request was successful, but no content is being returned.
	•	301 Moved Permanently: The resource has been permanently moved to a new URL.
	•	302 Found: The resource is temporarily located at a different URL.
	•	304 Not Modified: The resource has not been modified since the last request.
	•	400 Bad Request: The server could not understand the request due to invalid syntax.
	•	401 Unauthorized: Authentication is required to access the resource.
	•	403 Forbidden: The server understood the request but refuses to authorize it.
	•	404 Not Found: The requested resource could not be found.
	•	405 Method Not Allowed: The HTTP method is not allowed for the requested resource.
	•	409 Conflict: The request could not be completed due to a conflict with the current state of the resource.
	•	429 Too Many Requests: The user has sent too many requests in a given amount of time.
	•	500 Internal Server Error: The server encountered an unexpected condition that prevented it from fulfilling the request.
	•	502 Bad Gateway: The server received an invalid response from the upstream server.
	•	503 Service Unavailable: The server is temporarily unable to handle the request, often due to maintenance.
	•	504 Gateway Timeout: The server did not receive a timely response from an upstream server.

---

"""

"""
### Automating REST API Testing

To automate REST API testing, you can use Python's `requests` library. Below are examples of how to automate API requests including GET, POST, PUT, PATCH, and DELETE requests.

---
========================================================================================================================

### Example Code for Automating REST API Using Python

#### 1. **GET Request (Retrieve Data)**

"""

import requests

# API URL
url = "https://api.example.com/users"

# Headers with Authorization token
headers = {
    "Authorization": "Bearer your_access_token",
    "Content-Type": "application/json"
}

# Send GET request
response = requests.get(url, headers=headers)

# Check the response status
if response.status_code == 200:
    print("Response:", response.json())  # Print the JSON data
else:
    print(f"Error: {response.status_code}, {response.text}")

"""
========================================================================================================================

#### 2. **POST Request (Create Resource)**
"""


import requests

# API URL
url = "https://api.example.com/users"

# Data to be sent in the body
data = {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}

# Headers
headers = {
    "Authorization": "Bearer your_access_token",
    "Content-Type": "application/json"
}

# Send POST request
response = requests.post(url, json=data, headers=headers)

# Check if the resource was created
if response.status_code == 201:
    print("User created:", response.json())
else:
    print(f"Failed to create user: {response.status_code}, {response.text}")
"""
========================================================================================================================
#### 3. **PUT Request (Update Entire Resource)**

"""
import requests

# URL with path parameter for updating a specific user
url = "https://api.example.com/users/123"

# Updated data
data = {
    "name": "John Smith",
    "email": "john.smith@example.com",
    "age": 32
}

# Headers
headers = {
    "Authorization": "Bearer your_access_token",
    "Content-Type": "application/json"
}

# Send PUT request
response = requests.put(url, json=data, headers=headers)

# Check if the update was successful
if response.status_code == 200:
    print("User updated:", response.json())
else:
    print(f"Failed to update user: {response.status_code}, {response.text}")

"""
========================================================================================================================

#### 4. **PATCH Request (Partial Update)**
The PATCH method is used to partially update a resource. Unlike PUT, which replaces the entire resource, PATCH only updates the fields specified.

"""
import requests

# URL for the specific resource to update
url = "https://api.example.com/users/123"

# Partial update data
data = {
    "email": "new_email@example.com"
}

# Headers
headers = {
    "Authorization": "Bearer your_access_token",
    "Content-Type": "application/json"
}

# Send PATCH request
response = requests.patch(url, json=data, headers=headers)

# Check if the partial update was successful
if response.status_code == 200:
    print("User partially updated:", response.json())
else:
    print(f"Failed to partially update user: {response.status_code}, {response.text}")

"""
========================================================================================================================

5. **DELETE Request (Delete Resource)**

"""

import requests

# URL to delete a user with ID 123
url = "https://api.example.com/users/123"

# Headers
headers = {
    "Authorization": "Bearer your_access_token"
}

# Send DELETE request
response = requests.delete(url, headers=headers)

# Check if the deletion was successful (204 No Content)
if response.status_code == 204:
    print("User deleted successfully.")
else:
    print(f"Failed to delete user: {response.status_code}, {response.text}")



"""

### Key Considerations for API Automation

1. **Path Parameters**: Use path parameters in the URL to identify specific resources (e.g., `GET /users/123` to retrieve user with ID 123).

2. **PATCH Method**: The PATCH method is used for partial updates, which is efficient when only a small part of the resource needs to be changed. Use PATCH when updating individual fields rather than sending the full resource with PUT.

3. **Error Handling**: Ensure that your automation scripts handle different error scenarios by checking the status codes and response messages.

4. **Retry Logic**: Some APIs may be unreliable or slow. Implement retry mechanisms for certain error codes (e.g., 500 Internal Server Error or 503 Service Unavailable).

5. **Assertions**: Add assertions to your test scripts to validate that the response matches expected results. For example, after creating a user, you can assert that the returned user data matches what was sent in the request.

6. **Authentication**: Many APIs require authentication, typically via an OAuth token or API key. Automate the process of obtaining and refreshing tokens to ensure your tests are always authenticated.

---

### Tools for API Automation

1. **Postman**: A popular API development tool that lets you send requests and write automated tests. Collections can be executed programmatically using Postman's CLI tool, **Newman**.
2. **Newman**: Postman’s command-line tool for running API tests as part of your CI/CD pipeline.
3. **Requests Library**: A simple HTTP client for Python used to automate API requests.
4. **Tavern**: A pytest-based framework for testing RESTful APIs.
5. **Karate**: A tool designed for testing APIs, allowing you to script complex API test scenarios.

---

### Best Practices for API Automation

1. **Parameterization**: Use environment variables or config files to manage endpoint URLs, credentials, and other dynamic data.
2. **Test Data Management**: Ensure that the data used in tests is isolated, so it doesn't interfere with real production data.
3. **Continuous Integration**: Integrate your API tests with CI tools like Jenkins, GitLab CI, or CircleCI, and run them automatically when new changes are pushed.
4. **Monitor API Performance**: Implement tests that monitor the performance of the API, such as response times and rate limits.
5. **Security**: Avoid hard-coding sensitive information like tokens and API keys in your scripts. Instead, use secure storage solutions or environment variables.

---

By understanding and applying these REST API basics, including the proper use of path parameters, the PATCH method, and automating API tests with Python, you will have the ability to perform robust API testing. These practices are key to ensuring that your API remains functional and secure over time.

Let me know if you need further clarification or more examples!
"""