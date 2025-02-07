import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
name = 'Rahul'
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(4)
alert = driver.switch_to.alert
alertText = alert.text
print(alert.text)
assert name in alertText
alert.accept()

#alert.dismiss()

#Git test

