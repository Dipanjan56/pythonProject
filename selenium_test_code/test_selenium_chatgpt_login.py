import time

import undetected_chromedriver as uc
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element_to_be_visible(driver, element, timeout: int):
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(lambda d: element.is_displayed())
    except NoSuchElementException as e:
        print(f'element not found, Exception Type: {type(e).__name__}')


if __name__ == '__main__':

    driver = uc.Chrome()

    driver.maximize_window()
    driver.get("https://chatgpt.com/")
    driver.implicitly_wait(10)

    login_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='login-button']")
    login_button.click()

    username = driver.find_element(By.ID, 'email-input')
    wait_for_element_to_be_visible(driver, username, 3)
    username.send_keys('your_email')

    continue_button = driver.find_element(By.CSS_SELECTOR, '.continue-btn')
    continue_button.click()

    password = driver.find_element(By.ID, 'password')
    wait_for_element_to_be_visible(driver, password, 3)
    password.send_keys('your_password')

    login_button = driver.find_element(By.CSS_SELECTOR, '._button-login-password')
    login_button.click()

    code_input = driver.find_element(By.CSS_SELECTOR, "[class*='_codeInput']")
    wait_for_element_to_be_visible(driver, code_input, 3)
    code_input.send_keys('your_code')

    continue_button = driver.find_element(By.CSS_SELECTOR, "[class*='_continueButton']")
    continue_button.click()

    time.sleep(10)

    driver.quit()
