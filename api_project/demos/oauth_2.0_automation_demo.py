"""OAuth 2.0 Automation"""


"""
Automating OAuth 2.0 authentication using Python can be tricky because OAuth 2.0 often involves user consent and 
redirecting to a login page, which makes it hard to fully automate without manual intervention. 
However, there are ways to handle it programmatically depending on the OAuth 2.0 flow you are dealing with.

Common OAuth 2.0 Flows:

	1.	Authorization Code Grant (with user consent): Typically involves manual user consent in the browser.
	2.	Client Credentials Grant: No user interaction; often used for service-to-service communication.

Below is an example for automating both approaches:

1. Client Credentials Grant (Service-to-Service Communication)

This flow doesn’t require user interaction, so it can be fully automated. It is commonly used for server-to-server 
communication. The steps are:

	•	Exchange the client ID and client secret for an access token.
	•	Use the token to make API requests.

"""

import requests

# OAuth 2.0 token endpoint and credentials
token_url = "https://auth_server.com/oauth2/token"
client_id = "your_client_id"
client_secret = "your_client_secret"

# Request payload
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'your_scope'  # optional, depends on the API
}

# Request the token
response = requests.post(token_url, data=data)
token_response = response.json()

# Extract the access token
access_token = token_response.get("access_token")

# Use the access token to make authorized API requests
headers = {
    'Authorization': f"Bearer {access_token}"
}

# Example API request using the token
api_url = "https://api_server.com/protected/resource"
api_response = requests.get(api_url, headers=headers)

# Print the API response
print(api_response.json())