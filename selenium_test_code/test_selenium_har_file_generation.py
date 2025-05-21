import os
import time
from datetime import datetime

from selenium.common import NoSuchElementException, TimeoutException
from seleniumwire import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

import json


def wait_for_element_to_be_visible(driver, element, timeout: int):
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(lambda d: element.is_displayed())
    except NoSuchElementException as e:
        print(f'element not found, Exception Type: {type(e).__name__}')


def wait_and_get_element(driver, by, locator, timeout=5):
    """
    Waits for an element to be present in the DOM and returns it.
    Returns None if the element is not found within the timeout.

    :param driver: WebDriver instance
    :param by: selenium.webdriver.common.by.By
    :param locator: locator string (e.g., XPath or CSS)
    :param timeout: max wait time in seconds
    :return: WebElement or None
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        return element
    except TimeoutException:
        print(f"❌ Timeout: Element not found using {by} -> {locator}")
        return None


from urllib.parse import urlparse


def save_har_file(driver, filename="network_capture.har"):
    har_data = {
        "log": {
            "version": "1.2",
            "creator": {"name": "SeleniumWire", "version": "4.6.2"},
            "entries": []
        }
    }

    static_extensions = ('.js', '.css', '.png', '.jpg', '.jpeg', '.svg', '.ico', '.woff', '.woff2', '.ttf', '.eot')

    for request in driver.requests:
        if request.response:
            parsed_url = urlparse(request.url)
            if parsed_url.path.lower().endswith(static_extensions):
                continue  # Skip static resources

            request_headers = [{"name": k, "value": v} for k, v in request.headers.items()]
            response_headers = [{"name": k, "value": v} for k, v in request.response.headers.items()]

            post_data = None
            if request.method in ['POST', 'PUT', 'PATCH'] and request.body:
                try:
                    post_data = request.body.decode('utf-8')
                except Exception:
                    post_data = str(request.body)

            har_entry = {
                "startedDateTime": request.date.isoformat(),
                "time": 0,
                "request": {
                    "method": request.method,
                    "url": request.url,
                    "httpVersion": "HTTP/1.1",
                    "headers": request_headers,
                },
                "response": {
                    "status": request.response.status_code,
                    "statusText": request.response.reason,
                    "httpVersion": "HTTP/1.1",
                    "headers": response_headers,
                },
                "cache": {},
                "timings": {}
            }

            if post_data:
                har_entry["request"]["postData"] = {
                    "mimeType": request.headers.get("Content-Type", "application/octet-stream"),
                    "text": post_data
                }

            har_data["log"]["entries"].append(har_entry)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(har_data, f, indent=2)


def test_microsoft_copilot():
    start_time = time.time()
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.maximize_window()
    driver.get("https://copilot.microsoft.com/")
    driver.implicitly_wait(10)

    message_copilot = driver.find_element(By.ID, 'userInput')
    message_copilot.send_keys('What the capital of India?')
    message_copilot.send_keys(Keys.ENTER)

    copilot_said = wait_and_get_element(driver, By.XPATH, "//div/h2[text()='Copilot said']", 10)
    ai_message = wait_and_get_element(driver, By.CSS_SELECTOR, "[data-content='ai-message'] .break-words")
    end_suggestions = wait_and_get_element(driver, By.CSS_SELECTOR, ".mt-auto div")

    if copilot_said and ai_message and end_suggestions:
        print("✅ Copilot Answered")
    else:
        print("❌ Copilot response not detected")

    end_time = time.time()
    total_duration = round(end_time - start_time, 2)
    print(f"\n⏱️ Total time taken: {total_duration} seconds.")

    # Format HAR file name as microsoft_copilot_activity_21_May_11_56_09.har
    now = datetime.now()
    formatted_time = now.strftime("%d_%b_%H_%M_%S")
    har_file_name = f"microsoft_copilot_activity_{formatted_time}.har"
    har_folder_name = "har_files"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    har_path = os.path.join(current_dir, har_folder_name, har_file_name)
    os.makedirs(os.path.dirname(har_path), exist_ok=True)

    save_har_file(driver, har_path)

    driver.quit()


if __name__ == '__main__':
    options = Options()
    test_microsoft_copilot()
