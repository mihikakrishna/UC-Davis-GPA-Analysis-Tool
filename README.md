# UC Davis GPA Analysis Tool

## Overview

This project is a Python script for scraping and extracting GPA data from a website using Selenium. It automates the process of accessing a website, filling in login credentials, and extracting GPA information for various majors. The data is then stored in a CSV file.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium
- Chrome WebDriver
- Google Chrome browser (should be compaitble with Chrome WebDriver version)

Download the appropriate version of Chrome WebDriver and Chrome for Testing for your system and make sure to update their paths in `config.py`.

For more info on Chromedrivers and Chrome, please visit this website:  https://chromedriver.chromium.org/downloads

Additionally, you can install Selenium using pip:
```bash
pip install selenium 
```

## Usage
Clone this repository to your local machine.
Open the `config.py` file and update it with your login credentials

## Run the script:

```bash
python main.py
```
The script will automate the login process and start scraping GPA data. 
The data will be saved in a CSV file named `gpa_data.csv`.
Don't forget to accept DUO authentication when prompted!
