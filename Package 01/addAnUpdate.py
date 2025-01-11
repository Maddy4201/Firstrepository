import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = "https://aspx.co.in/login"
driver.get(url)
driver.maximize_window()
email_field = driver.find_element(By.XPATH, "//input[@id='email']")
email_field.send_keys("testonfourthdec@yopmail.com")
pwd_field = driver.find_element(By.XPATH, "//input[@id='password']")
pwd_field.send_keys("Mexico@#2024")
login_bttn = driver.find_element(By.CLASS_NAME, "submit-button")
login_bttn.click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='dynamic-offer-tooltip']//span[@aria-hidden='true'][normalize-space()='×']").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='Visit Your Website']").click()
# pages=driver.window_handles
# firstp=pages[0]
# secondp=pages[1]
# time.sleep(2)
# driver._switch_to.window(secondp)
# print("This is the title of user website: ",driver.title)
# time.sleep(5)
# driver._switch_to.window(firstp)
# print("This is the title of account page: ",driver.title)
driver.find_element(By.XPATH,"//span[normalize-space()='Updates/Posts']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Add Update/Post']").click()
driver.find_element(By.XPATH,"//input[@id='title']").send_keys("Prod2024")
driver.find_element(By.XPATH,"//div[@class='note-editable panel-body']").send_keys("Test Description")
driver.find_element(By.XPATH,"//button[@id='savePost']").click()
time.sleep(3)
newPost=driver.find_element(By.XPATH,"//ul[@class='timeline']//li[2]//h3")
print(newPost.text)
if newPost.text=="Prod2024":
	print("New Product addition verified")
else:
	print("Not verified")
