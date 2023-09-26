from selenium.webdriver.common.by import By

import selenium_utils
import scraper 

def main():
    driver = selenium_utils.setup_selenium()
    selenium_utils.login_to_website(driver)
    majors = scraper.extract_majors(driver)
    scraper.fetch_data_and_write_to_csv(driver, majors)
    driver.close()

if __name__ == "__main__":
    main()
