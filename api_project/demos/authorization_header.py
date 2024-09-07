import requests

# URL of the API endpoint
url = "https://api.example.com/users"

# Headers containing the Authorization token and Content-Type
headers = {
    "Authorization": "Bearer abc123xyz",  # Replace with your actual token
    "Content-Type": "application/json"
}

# Making the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse and print the JSON response from the server
    users = response.json()
    print(users)
else:
    print(f"Failed to retrieve users: {response.status_code}, {response.text}")