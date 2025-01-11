import time
from logging import exception

from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://aspx.co.in/")
currentHandle=driver.current_window_handle
driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
allHandles=driver.window_handles

for childHandle in allHandles:
	# print(childHandle)
	if currentHandle!=childHandle:
		driver._switch_to.window(childHandle)
try:
	driver.find_element(By.XPATH,"//input[@id='email']").send_keys("testuser12@yopmail.com")
	driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Testuser@1234")
	driver.find_element(By.XPATH,"//button[@class='submit-button']").click()
	print("Logged in by entering the details....")
	time.sleep(2)
	driver.find_element(By.XPATH,"//a[@class='callout-action']").click()
	driver.find_element(By.XPATH,"//span[@class='pp-plan yearly active']").click()
	time.sleep(2)
	driver.find_element(By.XPATH,"(//a[contains(text(),'Buy Subscription')])[1]").click()
	priceText = driver.find_element(By.XPATH,"//h4[@class='dash-dark-grey-text grand-total-align']")
	print("Price and currency is fetched and printed below...")
	print(priceText.text)
	time.sleep(4)
	driver.find_element(By.XPATH,"//button[@id='show-payment-pop-up']").click()
	time.sleep(3)
	priceonPage=driver.find_element(By.XPATH,"//h3[@id='formatted-grand-total']")
	print("Reconfirmation of Grand total: ", priceonPage.text)
	time.sleep(3)
	driver.find_element(By.ID,"razorpay-pay-btn-call").click()
	time.sleep(4)
except Exception as e:
	print("All good")
