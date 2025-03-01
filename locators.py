import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
# Id, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, 'email').send_keys('hello@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
driver.find_element(By.ID, 'exampleCheck1').click()

# Xpath - //tagname[@attribute='value'] -> "//input[@type='submit']" (//input[@type='text'])[3] when its the 3rd element
# CSS - tagname[attribute='value'] -> "//input[@type='submit']" #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Rahul Sheety')
driver.find_element(By.XPATH, "//input[@type='submit']" ).click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1" ).click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert 'Success' in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys('hello again')
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(10)