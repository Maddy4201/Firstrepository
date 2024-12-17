import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
myWait = WebDriverWait(driver, 10)
URL = "https://aspx.co.in/login"
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(10)
print("Title of this website is: ", driver.title)

test_data = {
    "valid": ["testonfourthdec@yopmail.com"],
    "invalid_data_types": ["123abc", "hello@world", "$%&*()"],
    # "boundary_values": ["", "A" * 256],  # Assuming max length is 255
    # "special_characters": ["<script>", "DROP TABLE users;"],
    "empty_whitespace": ["", " "],
}

for key, values in test_data.items():
    for value in values:
        # Re-fetch the elements inside the loop to avoid stale element reference
        email_field = driver.find_element(By.XPATH, "//input[@id='email']")
        pwd_field = driver.find_element(By.XPATH, "//input[@id='password']")
        login_bttn = driver.find_element(By.CLASS_NAME, "submit-button")

        if key == "valid":
            email_field.send_keys(value)
            pwd_field.send_keys("America@2024")
        else:
            email_field.clear()
            email_field.send_keys(value)
            pwd_field.clear()
            pwd_field.send_keys("Abcs1234")

        login_bttn.click()

        try:
            if key == "empty_whitespace" and not value.strip():
                # Wait specifically for the empty email error message
                email_error = myWait.until(
                    EC.presence_of_element_located((By.XPATH, "//strong[normalize-space()='The email field is required.']"))
                )
                print(f"Test case '{key}' with value '{value}' resulted in error: {email_error.text}")
            else:
                # Wait specifically for the general credentials error message
                error_message = myWait.until(
                    EC.presence_of_element_located((By.XPATH, "//strong[normalize-space()='These credentials do not match our records.']"))
                )
                print(f"Test case '{key}' with value '{value}' resulted in error: {error_message.text}")

        except Exception as e:
            # Only print an error if neither message was found, indicating another issue
            if key != "empty_whitespace" or value.strip():
                print(f"Test case '{key}' with value '{value}' did not trigger an expected error message: {e}")

        time.sleep(1)

driver.quit()
