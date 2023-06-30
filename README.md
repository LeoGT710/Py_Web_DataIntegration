# Py_Web_DataIntegration
Python Web Data Integration for Website Interaction and Google Sheets Analysis.
# Selenium Automation Script

This repository contains a Python script that demonstrates automation using the Selenium WebDriver. The script performs a series of actions on a web application, such as logging in, navigating to specific pages, interacting with elements, and exporting data to Excel.

## Prerequisites

To run this script, make sure you have the following installed:

- Python (version 3.6 or higher)
- Selenium WebDriver for Python
- Chrome web browser

You can install Selenium using the following command:
pip install selenium


## Setup

1. Clone this repository to your local machine or download the script file.
2. Ensure that you have Chrome installed on your system.
3. Download the ChromeDriver executable compatible with your Chrome version from the [official ChromeDriver website](https://sites.google.com/a/chromium.org/chromedriver/downloads).
4. Extract the downloaded ChromeDriver executable and note down its file path.
5. Open the script file in a text editor.
6. Update the `chrome_driver_path` variable with the file path of the ChromeDriver executable you downloaded in the previous step.
7. Optionally, update the download directory path and other preferences in the `chrome_options` section based on your requirements.

## Usage

1. Open a terminal or command prompt and navigate to the directory containing the script.
2. Run the following command to execute the script: python script.py


The script will launch a headless Chrome browser and perform the automation steps defined in the script.

3. Monitor the terminal output to track the progress of the script.
4. After completion, the script will export data to an Excel file in the specified download directory.

## Notes

- Make sure the website URLs (`login_url`, `website_url`, `details_page_url_pattern`) in the script are valid and accessible.
- Update the login credentials (`username_input.send_keys('admin')` and `password_input.send_keys('Mrn00dle@')`) in the script to match your actual credentials.
- Adjust the mouse click coordinates (`click_x` and `click_y`) if needed, to interact with specific elements accurately.
- Modify the wait durations (`time.sleep()`) if necessary, to ensure proper page loading and element visibility.
- Customize the script as per your requirements, adding or modifying actions using Selenium WebDriver functions.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the script according to your needs.



