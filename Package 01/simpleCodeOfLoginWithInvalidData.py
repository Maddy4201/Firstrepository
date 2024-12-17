import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
URL = "https://aspx.co.in/login"
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(10)
print("Title of this website is: ", driver.title)

test_data = {
	"valid": ["ValidInput"],
	"invalid_data_types": ["123abc", "hello@world", "$%&*()"],
	# "boundary_values": ["", "A" * 256],  # Assuming max length is 255
	"special_characters": ["<script>", "DROP TABLE users;"],
	"empty_whitespace": ["", " "],
}

for key, values in test_data.items():
	for value in values:
		# Re-fetch the elements inside the loop to avoid stale element reference
		email_field = driver.find_element(By.XPATH, "//input[@id='email']")
		pwd_field = driver.find_element(By.XPATH, "//input[@id='password']")
		login_bttn = driver.find_element(By.CLASS_NAME, "submit-button")

		email_field.send_keys(value)
		pwd_field.send_keys("Abcs1234")
		login_bttn.click()

		try:
			error_message = driver.find_element(By.XPATH,
												"//strong[normalize-space()='These credentials do not match our records.']")
			print(f"Test case '{key}' with value '{value}' resulted in error: {error_message.text}")
		except:
			print(f"Test case '{key}' with value '{value}' did not trigger an error message")

		time.sleep(1)

driver.quit()
