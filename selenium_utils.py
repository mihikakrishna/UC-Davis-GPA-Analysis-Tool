from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

import config

def setup_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = config.CHROME_BINARY_PATH
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    service = Service(config.CHROME_DRIVER_PATH)
    return webdriver.Chrome(service=service, options=chrome_options)

def login_to_website(driver):
    driver.get(config.BASE_URL)

    username_elem = driver.find_element(By.NAME, "username")
    password_elem = driver.find_element(By.NAME, "password")

    username_elem.send_keys(config.USERNAME)
    password_elem.send_keys(config.PASSWORD)
    password_elem.send_keys(Keys.RETURN)

    sleep(5)

    driver.switch_to.frame("duo_iframe")
    button = driver.find_element(By.CSS_SELECTOR, ".auth-button.positive")
    button.click()
    
    sleep(15)

    driver.switch_to.default_content()
