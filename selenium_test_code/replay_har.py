import json
import requests
import time
from urllib.parse import urlparse

def load_and_replay_har(filename: str, filter_domain: str = "copilot.microsoft.com", print_response: bool = False):
    start_time = time.time()

    # Load HAR file
    with open(filename, 'r', encoding='utf-8') as f:
        har_data = json.load(f)

    entries = har_data['log']['entries']
    request_count = 0

    for i, entry in enumerate(entries):
        req = entry['request']
        method = req['method']
        url = req['url']

        # Skip WebSocket requests
        if url.startswith("wss://"):
            print(f"\n⚠️  Skipping WebSocket request: {url}")
            continue

        # Only replay requests for the filtered domain
        if filter_domain not in url:
            continue

        # Skip static resources
        parsed = urlparse(url)
        if parsed.path.endswith(('.js', '.css', '.png', '.jpg', '.svg', '.ico', '.woff', '.woff2')):
            continue

        headers = {
            h['name']: h['value']
            for h in req['headers']
            if h['name'].lower() not in ['cookie', 'authorization']
        }

        post_data = None
        if method in ['POST', 'PUT', 'PATCH']:
            try:
                post_data = req.get('postData', {}).get('text', None)
            except Exception as e:
                print(f"    ➤ Error reading postData: {e}")

        print(f"\n➡️ Replaying Request {i + 1}: {method} {url}")
        try:
            response = requests.request(method, url, headers=headers, data=post_data, timeout=10)
            print(f"    ✅ Status: {response.status_code}")
            request_count += 1
            if print_response:
                print("    🔁 Response Body Preview:")
                content_type = response.headers.get('Content-Type', '')
                if 'application/json' in content_type:
                    try:
                        print(json.dumps(response.json(), indent=2))
                    except Exception:
                        print("    [Could not decode JSON response]")
                else:
                    print(response.text[:500])
        except Exception as e:
            print(f"    ❌ Error: {e}")

    end_time = time.time()
    total_duration = round(end_time - start_time, 2)
    print(f"\n⏱️ Replayed {request_count} requests in {total_duration} seconds.")


if __name__ == '__main__':
    har_file_path = '/selenium_test_code/har_files/microsoft_copilot_activity_1.har'
    load_and_replay_har(har_file_path, print_response=False)