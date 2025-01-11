import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, ElementNotInteractableException

# Helper function to check element presence
def is_element_present(driver, by, value):
    try:
        element = driver.find_element(by, value)
        return element
    except NoSuchElementException:
        return None

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = "https://aspx.co.in/login"
driver.get(url)
driver.maximize_window()

try:
    # Login steps
    email_field = driver.find_element(By.XPATH, "//input[@id='email']")
    email_field.send_keys("testuser12@yopmail.com")

    pwd_field = driver.find_element(By.XPATH, "//input[@id='password']")
    pwd_field.send_keys("Testuser@1234")

    login_bttn = driver.find_element(By.CLASS_NAME, "submit-button")
    login_bttn.click()
    time.sleep(2)

    # Handle login popup
    login_popup = is_element_present(driver, By.XPATH, "//h3[normalize-space()='Congratulations!']")
    if login_popup and login_popup.is_displayed():
        close_button = is_element_present(driver, By.XPATH, "//a[@onclick='closeWebsiteCreateMessageModal()']")
        if close_button:
            close_button.click()
        time.sleep(2)

    # Handle new popup
    new_popup = is_element_present(driver, By.XPATH, "//div[@class='driver-popover']")
    if new_popup and new_popup.is_displayed():
        close_button = is_element_present(driver, By.XPATH, "//button[@class='driver-popover-close-btn']")
        if close_button:
            close_button.click()
        time.sleep(1)

    # Navigate to business card
    busi_card = is_element_present(driver, By.XPATH, "//a[@id='business_card_nav']")
    time.sleep(2)
    if busi_card and busi_card.is_enabled():
        bogo_close_button = is_element_present(driver, By.XPATH, "//button[@class='close __bogo_popup_close_event']")
        if bogo_close_button:
            bogo_close_button.click()
        user_image = is_element_present(driver, By.XPATH, "//img[@class='user-image']")
        if user_image:
            user_image.click()
        time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

# Handle Sign Out
try:
    # Wait until "Sign out" is clickable
    wait = WebDriverWait(driver, 10)
    sign_out = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sign out']")))

    # Scroll to the "Sign out" button
    driver.execute_script("arguments[0].scrollIntoView(true);", sign_out)

    # Click the "Sign out" button
    sign_out.click()
    time.sleep(3)
    print("This test was running on", driver.name, "driver")
    print("Login is successful....")
except (ElementNotInteractableException, NoSuchElementException) as e:
    print(f"Sign out interaction error: {e}")

# Quit the driver
driver.quit()
