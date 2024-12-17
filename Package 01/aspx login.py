import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = "https://aspx.co.in/login"
driver.get(url)
driver.maximize_window()

try:
	email_field = driver.find_element(By.XPATH, "//input[@id='email']")
	email_field.send_keys("testuser12@yopmail.com")

	pwd_field = driver.find_element(By.XPATH, "//input[@id='password']")
	pwd_field.send_keys("Testuser@1234")

	login_bttn = driver.find_element(By.CLASS_NAME, "submit-button")
	login_bttn.click()
	time.sleep(2)

	try:
		login_popup = driver.find_element(By.XPATH, "//h3[normalize-space()='Congratulations!']")
		if login_popup.is_displayed():
			driver.find_element(By.XPATH, "//a[@onclick='closeWebsiteCreateMessageModal()']").click()
			time.sleep(2)
	except (ElementNotInteractableException, NoSuchElementException) as e:
		print(f"Login popup interaction error: {e}")

	try:
		new_popup = driver.find_element(By.XPATH, "//div[@class='driver-popover']")
		if new_popup.is_displayed():
			driver.find_element(By.XPATH, "//button[@class='driver-popover-close-btn']").click()
			time.sleep(1)
	except (ElementNotInteractableException, NoSuchElementException) as e:
		print(f"New popup interaction error: {e}")

	busi_card = driver.find_element(By.XPATH, "//a[@id='business_card_nav']")
	time.sleep(2)
	if busi_card.is_enabled():
		driver.find_element(By.XPATH,"//button[@class='close __bogo_popup_close_event']").click()
		driver.find_element(By.XPATH, "//img[@class='user-image']").click()
		time.sleep(2)

except Exception as e:
	print(f"An error occurred: {e}")

try:
	driver.find_element(By.XPATH, "//a[normalize-space()='Sign out']").click()
	time.sleep(3)
	print("This test was running on", driver.name, "driver")
	print("Login is successful....")
except (ElementNotInteractableException, NoSuchElementException) as e:
	print(f"Sign out interaction error: {e}")

driver.quit()
