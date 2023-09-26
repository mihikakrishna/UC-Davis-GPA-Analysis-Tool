from selenium.webdriver.common.by import By
from time import sleep

import csv
import re

import config

def extract_majors(driver):
    majors = []
    
    # Find all options within the dropdown list(s)
    major_options = driver.find_elements(By.CSS_SELECTOR, "option")
    
    # Iterate over each option and store its value and text
    for option in major_options:
        major_code = option.get_attribute("value")
        majors.append(major_code)
        
    return majors

def extract_data_from_table(driver):
    data = []
    table_rows = driver.find_elements(By.CSS_SELECTOR, ".jqplot-table-legend tr.jqplot-table-legend")

    for row in table_rows[1:]:
        text = row.find_element(By.CSS_SELECTOR, '.jqplot-table-legend-label').text

        major = re.search(r"(.*?) \(", text).group(1)
        course_code = re.search(r"\((.*?)\)", text).group(1)
        gpa = float(re.search(r"- (\d+\.\d+)", text).group(1))
        students = int(re.search(r"Based on (\d+) student", text).group(1))

        data.append({
            'College': config.COLLEGES_DICT[course_code[0]],
            'Major': major,
            'Course Code': course_code,
            'Average GPA': gpa,
            'Number of Students': students
        })

    return data


def fetch_data_and_write_to_csv(driver, majors):
    # Open the CSV file for writing
    with open('gpa_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['College', 'Major', 'Course Code', 'Average GPA', 'Number of Students'])  # Write the csv headers
        
        # Loop through each group of majors
        for i in range(0, len(majors), config.MAX_MAJORS_PER_ITERATION):
                majors_by_10 = majors[i : i + config.MAX_MAJORS_PER_ITERATION]

                url = config.BASE_URL + "%2C".join(majors_by_10)
                print(f"Scraping URL : {url}\n")
                driver.get(url)

                sleep(5)

                data = extract_data_from_table(driver)
                for item in data:
                    writer.writerow([item['College'], item['Major'],  item['Course Code'], item['Average GPA'], item['Number of Students']])


        