import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, TimeoutException


def get_locators_in_simple_format(url: str) -> str:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

    driver = None
    results = []  # This will store the flat list of locator dictionaries

    try:
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(30)
        try:
            driver.get(url)
            time.sleep(5)
        except TimeoutException:
            return json.dumps([{"error": f"Timeout loading URL: {url}"}], indent=2)

        driver.implicitly_wait(3)

        all_elements_on_page = driver.find_elements(By.XPATH, "//*")

        processed_elements_identifiers = set()  # To avoid duplicate entries if multiple strategies point to same logical element representation

        for element in all_elements_on_page:
            try:
                if not element.is_displayed():
                    continue

                tag_name = element.tag_name.lower()
                element_id = element.get_attribute("id")
                element_name = element.get_attribute("name")

                element_text_content = ""
                try:
                    if tag_name in ["input", "textarea"]:  # For inputs, value attribute is often more relevant
                        element_text_content = element.get_attribute("value") or ""
                    if not element_text_content:  # Fallback to textContent
                        element_text_content = driver.execute_script("return arguments[0].textContent;", element) or ""

                    element_text_content = element_text_content.strip().replace('\n', ' ').replace('\r', '')
                    if len(element_text_content) > 100:  # Trim very long text
                        element_text_content = element_text_content[:97] + "..."
                except (StaleElementReferenceException, WebDriverException):
                    element_text_content = ""  # Cannot fetch text

                # --- Strategy 1: Unique ID ---
                if element_id:
                    locator_key = f"id_{element_id}"
                    if locator_key not in processed_elements_identifiers:
                        try:
                            if len(driver.find_elements(By.ID, element_id)) == 1:
                                results.append({
                                    "locator": element_id,
                                    "locatortype": "id",
                                    "locatorvalue": element_id
                                })
                                processed_elements_identifiers.add(locator_key)
                                continue  # Prioritize this and move to next element
                        except (WebDriverException, StaleElementReferenceException):
                            pass

                # --- Strategy 2: Unique Name ---
                if element_name:
                    locator_key = f"name_{element_name}"
                    if locator_key not in processed_elements_identifiers:
                        try:
                            if len(driver.find_elements(By.NAME, element_name)) == 1:
                                results.append({
                                    "locator": element_name,
                                    "locatortype": "name",
                                    "locatorvalue": element_name
                                })
                                processed_elements_identifiers.add(locator_key)
                                continue
                        except (WebDriverException, StaleElementReferenceException):
                            pass

                # --- Strategy 3: Link Text for <a> tags ---
                if tag_name == 'a' and element_text_content:
                    clean_text = element_text_content.strip()
                    if clean_text and 0 < len(clean_text) < 70 and "..." not in clean_text:
                        locator_key = f"linktext_{clean_text}"
                        if locator_key not in processed_elements_identifiers:
                            try:
                                # Check for exact match link text uniqueness
                                if len(driver.find_elements(By.LINK_TEXT, clean_text)) == 1:
                                    results.append({
                                        "locator": clean_text,
                                        "locatortype": "linkText",
                                        "locatorvalue": clean_text
                                    })
                                    processed_elements_identifiers.add(locator_key)
                                    continue
                            except (WebDriverException, StaleElementReferenceException):
                                pass

                # --- Strategy 4: Text on button-like elements using XPath ---
                is_button_like = tag_name == 'button' or \
                                 element.get_attribute('role') == 'button' or \
                                 (tag_name == 'input' and element.get_attribute('type') in ['submit', 'button',
                                                                                            'reset'])

                if is_button_like and element_text_content:
                    clean_text = element_text_content.strip()
                    # Use visible text if 'value' attribute was empty or not applicable (e.g. <button>Text</button>)
                    if not clean_text and tag_name == 'button':  # check textContent again if value was empty for button
                        current_text_content = (
                                    driver.execute_script("return arguments[0].textContent;", element) or "").strip()
                        if current_text_content and 0 < len(
                                current_text_content) < 70 and "..." not in current_text_content:
                            clean_text = current_text_content

                    if clean_text and 0 < len(clean_text) < 70 and "..." not in clean_text:
                        locator_key = f"buttontext_{clean_text}"
                        if locator_key not in processed_elements_identifiers:
                            xpath_val = ""
                            # Construct XPath for text, handling quotes
                            if "'" in clean_text and '"' in clean_text:
                                parts = clean_text.split("'")
                                concat_parts = []
                                for i_part, part in enumerate(parts):
                                    if part: concat_parts.append(f'"{part}"')
                                    if i_part < len(parts) - 1: concat_parts.append("'\"'\"'")
                                if concat_parts: xpath_val = f".//self::{tag_name}[normalize-space()=concat({','.join(concat_parts)})]"
                            elif "'" in clean_text:
                                xpath_val = f'.//self::{tag_name}[normalize-space()="{clean_text}"]'
                            else:
                                xpath_val = f".//self::{tag_name}[normalize-space()='{clean_text}']"

                            if xpath_val:
                                try:
                                    # Check if this XPath is reasonably unique (e.g., finding 1 element from current context)
                                    # For simplicity, we assume if text is distinct, it's a good candidate
                                    # A full uniqueness check `driver.find_elements(By.XPATH, global_xpath_val)` can be slow
                                    results.append({
                                        "locator": clean_text,
                                        "locatortype": "xpath",
                                        "locatorvalue": xpath_val.replace(".//self::", "//")
                                        # Make it a global path for general use
                                    })
                                    processed_elements_identifiers.add(locator_key)
                                    continue
                                except (WebDriverException, StaleElementReferenceException):
                                    pass

                # --- Fallback/Alternative: Add non-unique IDs/Names if not already added as unique ---
                # This ensures that if an ID or Name exists but wasn't unique, it's still captured.
                if element_id:
                    locator_key = f"id_{element_id}"
                    if locator_key not in processed_elements_identifiers:
                        results.append({
                            "locator": f"{element_id} (id, non-unique)",
                            "locatortype": "id",
                            "locatorvalue": element_id
                        })
                        processed_elements_identifiers.add(locator_key)
                        # Don't 'continue' here, as other locators might also be relevant

                if element_name:
                    locator_key = f"name_{element_name}"
                    if locator_key not in processed_elements_identifiers:
                        results.append({
                            "locator": f"{element_name} (name, non-unique)",
                            "locatortype": "name",
                            "locatorvalue": element_name
                        })
                        processed_elements_identifiers.add(locator_key)

            except StaleElementReferenceException:
                continue
            except WebDriverException as wd_ex:
                # Log minimal error if needed, but continue processing other elements
                # print(f"Minor WebDriverException for an element: {str(wd_ex)[:100]}")
                continue

        return json.dumps(results, indent=2)

    except WebDriverException as e:
        return json.dumps([{"error": f"A WebDriverException occurred: {str(e)}", "url": url}], indent=2)
    except Exception as e:
        return json.dumps([{"error": f"An unexpected error occurred: {str(e)}", "url": url}], indent=2)
    finally:
        if driver:
            driver.quit()


if __name__ == '__main__':
    # Test with a sample URL that has forms and links
    # test_url = "https://trytestingthis.netlify.app/"
    test_url = "https://copilot.microsoft.com/" # A test login page
    # test_url = "https://www.wikipedia.org/"

    # Example from user query (assuming a page like it)
    # For "http://eaapp.somee.com/" the output would be closer to the example
    # if elements UserName, Password, RememberMe (ids) and "Log in" (button/link) exist.

    print(f"Fetching locators in simple format for: {test_url}")
    locators_output_json = get_locators_in_simple_format(test_url)
    print(locators_output_json)

    # To save to a file:
    with open("locators_simple_output.json", "w", encoding="utf-8") as f:
        f.write(locators_output_json)
    print("\nOutput saved to locators_simple_output.json")

    # Example for user input:
    # user_provided_url = input("\nEnter a webpage URL (e.g., https://www.google.com): ")
    # if user_provided_url:
    #     print(f"\nFetching locators for: {user_provided_url}")
    #     user_locators_json = get_locators_in_simple_format(user_provided_url)
    #     print(user_locators_json)
    #     with open("user_locators_simple_output.json", "w", encoding="utf-8") as f:
    #         f.write(user_locators_json)
    #     print("\nUser URL output saved to user_locators_simple_output.json")