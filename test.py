from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set up Chrome WebDriver with Headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

# Chrome Headless shell path
chrome_binary_path = r"C:\Users\atish\Downloads\chrome-headless-shell-win64\chrome-headless-shell-win64\chrome-headless-shell.exe"
options.binary_location = chrome_binary_path

# ChromeDriver path
service = Service(r"C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

try:
    # Step 1: Navigate to Gmail
    driver.get("https://www.gmail.com")
    print("Page title is:", driver.title)

    # Step 2: Enter email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_input.send_keys("aj722@snu.edu.in")
    email_input.send_keys(Keys.RETURN)
    print("Email entered successfully")

    # Step 3: Wait for password field and enter password
    # Using a more specific selector for the password field
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    password_input.send_keys("DadriIndirapuram123")  # Replace with actual password
    password_input.send_keys(Keys.RETURN)
    print("Password entered")

    # Step 4: Wait for successful login
    WebDriverWait(driver, 10).until(
        EC.url_contains("mail.google.com/mail")
    )
    print("Successfully logged into Gmail!")

    # Create screenshots directory if it doesn't exist
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Take a screenshot of the inbox
    time.sleep(2)  # Wait for inbox to fully load
    driver.save_screenshot("screenshots/gmail_inbox.png")
    print("Screenshot saved")

except Exception as e:
    print("Test failed:", str(e))
    # Save error screenshot
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    driver.save_screenshot("screenshots/error_screenshot.png")
    print("Error screenshot saved")

finally:
    driver.quit()
    print("Test completed.")