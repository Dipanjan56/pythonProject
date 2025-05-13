import time

from selenium.common import NoSuchElementException, TimeoutException
from seleniumwire import webdriver  # <-- use seleniumwire
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
    message_copilot.send_keys('What is the weather today?')
    message_copilot.send_keys(Keys.ENTER)

    copilot_said = wait_and_get_element(driver, By.XPATH, "//div/h2[text()='Copilot said']", 10)

    if copilot_said:
        print("✅ Copilot Answered")
    else:
        print("❌ Copilot response not detected")

    end_time = time.time()
    total_duration = round(end_time - start_time, 2)
    print(f"\n⏱️ Total time taken: {total_duration} seconds.")

    save_har_file(driver,
                  "/Users/dkundu/projects/personal_projects/pythonProject/selenium_test_code/har_files/microsoft_copilot_activity.har")

    driver.quit()


if __name__ == '__main__':
    options = Options()
    test_microsoft_copilot()
