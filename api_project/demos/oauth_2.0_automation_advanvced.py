import os
import requests
import time

# Load client credentials securely from environment variables
client_id = os.getenv("OAUTH_CLIENT_ID")
client_secret = os.getenv("OAUTH_CLIENT_SECRET")
token_url = "https://auth_server.com/oauth2/token"

# Request a token using the client credentials grant
def get_access_token():
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'read_only_scope'  # Use the least privilege
    }
    response = requests.post(token_url, data=data)

    if response.status_code != 200:
        print(f"Failed to fetch access token: {response.status_code}, {response.text}")
        return None

    token_response = response.json()
    access_token = token_response.get("access_token")
    expires_in = token_response.get("expires_in")
    token_creation_time = time.time()

    return access_token, expires_in, token_creation_time

# Check if token is expired
def is_token_expired(token_creation_time, expires_in):
    return time.time() > token_creation_time + expires_in

# Use the access token to make authorized API calls
def fetch_protected_data(api_url, access_token):
    headers = {
        'Authorization': f"Bearer {access_token}"
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"API request failed: {response.status_code}, {response.text}")
        return None

# Main flow
def main():
    api_url = "https://api_server.com/protected/resource"

    # Fetch a token
    access_token, expires_in, token_creation_time = get_access_token()

    if access_token:
        # Use the token before it expires
        if not is_token_expired(token_creation_time, expires_in):
            protected_data = fetch_protected_data(api_url, access_token)
            print(protected_data)
        else:
            print("Token expired")
    else:
        print("Failed to obtain access token")

if __name__ == "__main__":
    main()