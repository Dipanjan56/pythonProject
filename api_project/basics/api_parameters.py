"""API Parameters """

"""
APIs (Application Programming Interfaces) often accept various types of parameters to control the behavior of the request and response.
These parameters allow the client to send data, filter results, set preferences, and more. There are generally **four** main types of parameters in APIs:

### 1. **Path Parameters**
   - **Description**: Path parameters are part of the URL and typically represent resource identifiers.
   They are often used to identify specific resources.
   - **Usage**: Path parameters are required and appear in the URL path.
   - **Example**:
     ```
     GET /users/{user_id}
     ```
     Here, `{user_id}` is a path parameter. A real request might look like this:
     ```
     GET /users/123
     ```
     - **Explanation**: The API returns the details of the user with ID `123`.

---

### 2. **Query Parameters**
   - **Description**: Query parameters are optional parameters that appear at the end of the URL and are typically used to filter, sort, or paginate resources. They are sent after a `?` and multiple query parameters are separated by `&`.
   - **Usage**: Query parameters are optional and often used to refine the results of the request.
   - **Example**:
     ```
     GET /users?age=30&city=NewYork
     ```
     - **Explanation**: This query requests a list of users who are 30 years old and live in New York. `age` and `city` are query parameters.

---

### 3. **Header Parameters**
   - **Description**: Header parameters are included in the request headers and typically contain metadata, like API keys, content type, authentication tokens, etc.
   - **Usage**: Header parameters are often used for authentication, content negotiation, and session management.
   - **Example**:
     ```
     GET /users
     Headers:
     Authorization: Bearer {token}
     Content-Type: application/json
     ```
     - **Explanation**: The API request contains an authorization token in the header (`Authorization: Bearer {token}`), indicating that the request is authenticated. The `Content-Type` header tells the server that the content is in JSON format.

---

### 4. **Body Parameters**
   - **Description**: Body parameters are sent in the body of the request and are typically used in POST, PUT, PATCH, and DELETE requests. They contain the data you want to send to the server.
   - **Usage**: These are commonly used when submitting data to create or update resources.
   - **Example**:
     ```
     POST /users
     Body:
     {
         "name": "John Doe",
         "age": 30,
         "email": "john@example.com"
     }
     ```
     - **Explanation**: This request creates a new user with the provided details (name, age, email) in the body of the request.

---

### 5. **Matrix Parameters** (less common)
   - **Description**: Matrix parameters are similar to query parameters but are embedded within the URL path.
   - **Usage**: They are rarely used, but some APIs employ them for filtering.
   - **Example**:
     ```
     GET /users;age=30;city=NewYork
     ```
     - **Explanation**: This query filters users by age and city but uses matrix parameters embedded in the URL rather than query parameters.

---

### Detailed Examples:

#### 1. **Path Parameter Example:**
   ```http
   GET /users/123
   ```
   - Retrieves the user with ID `123`.

#### 2. **Query Parameter Example:**
   ```http
   GET /users?age=25&status=active
   ```
   - Retrieves users who are 25 years old and have an active status.

#### 3. **Header Parameter Example:**
   ```http
   GET /users
   Headers:
   Authorization: Bearer abc123xyz
   Accept: application/json
   ```
   - The request includes an authorization token (`abc123xyz`) and specifies that it accepts a JSON response.

#### 4. **Body Parameter Example (for POST or PUT requests):**
   ```http
   POST /users
   Body:
   {
       "name": "Alice",
       "email": "alice@example.com",
       "age": 28
   }
   ```
   - Sends user data in the request body to create a new user.

---

### Overview of Parameters:
| Type             | Location                    | Common Usage                                  | Example                                                |
|------------------|-----------------------------|-----------------------------------------------|--------------------------------------------------------|
| Path Parameters  | Part of the URL             | Identify specific resource                    | `/users/{user_id}` (`/users/123`)                      |
| Query Parameters | After `?` in the URL        | Filter, sort, paginate                        | `/users?age=25&city=NewYork`                           |
| Header Parameters| HTTP Headers                | Authentication, Content-Type, custom metadata | `Authorization: Bearer abc123`, `Content-Type: application/json` |
| Body Parameters  | Request body (POST/PUT)     | Create or update resources                    | `{ "name": "John", "age": 30 }`                        |
| Matrix Parameters| Embedded in the URL (rare)  | Alternative to query parameters               | `/users;age=30;city=NewYork`                           |

### Choosing Parameter Types:
- **Path Parameters**: Use for essential resource identification.
- **Query Parameters**: Use for filtering, sorting, and optional information.
- **Header Parameters**: Use for authentication and metadata.
- **Body Parameters**: Use for submitting data to create or update resources.

Let me know if you need further clarification or more examples!
"""