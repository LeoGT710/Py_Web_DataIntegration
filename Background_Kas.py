import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")

# Set Chrome's default download directory
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r'C:\Users\hvle\Downloads',
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
})

# Initialize the Selenium WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Execute JavaScript to set download behavior
params = {
    "behavior": "allow",
    "downloadPath": r"C:\Users\hvle\Downloads"
}
driver.execute_cdp_cmd("Page.setDownloadBehavior", params)


login_url = 'http://mrsteak.kasco.vn/kas/Admin/Login'
website_url = 'http://mrsteak.kasco.vn/kas/Admin/SiteChoosen'
details_page_url_pattern = 'http://mrsteak.kasco.vn/kas/Admin/Home'

# Open the login page
print("Opening the login page...")
driver.get(login_url)

# Find the username and password input fields and fill in the credentials
print("Entering login credentials...")
username_input = driver.find_element(By.ID, 'login-username')
password_input = driver.find_element(By.ID, 'login-password')
username_input.send_keys('admin')
password_input.send_keys('Mrn00dle@')

# Submit the login form
print("Submitting login form...")
submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()

# Wait for the login to complete and redirect to the desired page
wait = WebDriverWait(driver, 60)
wait.until(EC.url_to_be(website_url))
print("Login successful.")

# Perform actions on the desired page after successful login
element = wait.until(EC.presence_of_element_located((By.XPATH, '//h5[contains(text(), "MS04 - GOC Coffee & Tea - Tân Phước")]')))
print('Element text:', element.text)

# Click on the element to navigate to its details page
print("Clicking on the element...")
element.click()

# Wait for the URL to contain the expected pattern
wait.until(EC.url_contains(details_page_url_pattern))
print('Details page URL:', driver.current_url)

# Switch to the newly opened window or tab
driver.switch_to.window(driver.window_handles[-1])
driver.maximize_window()

# Find and click on the <span>Báo cáo phân tích</span> element
bao_cao_element = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Báo cáo phân tích")]')))
print("Clicking on 'Báo cáo phân tích' element...")
bao_cao_element.click()

# Wait for the URL to match the details page pattern
wait.until(EC.url_to_be(details_page_url_pattern))

# Find and click on the <a> element
report_element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "RevenueByProduct03")]')))
print("Clicking on the report element...")
report_element.click()

# Switch to the newly opened window or tab
driver.switch_to.window(driver.window_handles[-1])

# Find and click on the <i> element
element_to_click = wait.until(EC.presence_of_element_located((By.XPATH, '//i[contains(@class, "icon") and contains(@class, "fa") and contains(@class, "fa-search")]')))
print("Clicking on the search icon...")
element_to_click.click()
element_to_click.click()

# Use ActionChains to send "Tab" key to move to the next field
ActionChains(driver).send_keys(Keys.TAB).perform()

# Switch back to the current active element
current_field = driver.switch_to.active_element
current_field.click()
current_field.click()

# Clear the current field
current_field.clear()
current_field.send_keys('25/06/2023 00:00')
ActionChains(driver).send_keys(Keys.ENTER).perform()

# Use ActionChains to send "Tab" key to move to the next field
ActionChains(driver).send_keys(Keys.TAB).perform()

# Switch back to the current active element
current_field = driver.switch_to.active_element
current_field.send_keys('26/06/2023 23:59')
ActionChains(driver).send_keys(Keys.ENTER).perform()

# Use ActionChains to send "Tab" key to move to the next field
ActionChains(driver).send_keys(Keys.TAB).perform()

# Switch back to the current active element
current_field = driver.switch_to.active_element

# Clear the current field
current_field.clear()
current_field.send_keys('MS04 - GOC Coffee & Tea - Tân Phước')
ActionChains(driver).send_keys(Keys.ENTER).perform()

# Use ActionChains to send "Tab" key to move to the next field
ActionChains(driver).send_keys(Keys.TAB).perform()

# Switch back to the current active element
current_field = driver.switch_to.active_element

window_size = driver.get_window_size()
click_x = 50  # Adjust the x-coordinate as needed
click_y = 50  # Adjust the y-coordinate as needed
actual_x = int(window_size['width'] * click_x / 100)
actual_y = int(window_size['height'] * click_y / 100)

try:
    # Perform the click action using ActionChains
    actions = ActionChains(driver)
    actions.move_by_offset(actual_x, actual_y).click().perform()
except:
    print("Error: Click coordinates are out of bounds")

input_element = driver.find_element(By.XPATH, '//input[contains(@class, "inputControl")]')
input_value = input_element.get_attribute('value')
print('Input value:', input_value)

second_input_element = driver.find_element(By.XPATH, '//input[contains(@data-content, "Đến ngày giờ")]')
print("Input value:", second_input_element.get_attribute("value"))

element = driver.find_element(By.XPATH, '//input[@class="select2-search__field"]')
print("Input value:", element.get_attribute("innerText"))





# Wait for the export button to be clickable

time.sleep(10)
# Wait for the export button to be clickable

# Wait for the export button to be present and visible
export_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class, "itemBtnGroup")]//span[contains(@class, "title") and text()="Xuất ra excel"]')))

# Scroll to the export button
driver.execute_script("arguments[0].scrollIntoView(true);", export_button)

time.sleep(10)

# Click on the export button
export_button.click()



time.sleep(100)
# Close the browser
driver.quit()


