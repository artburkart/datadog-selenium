from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://app.datadoghq.com/account/login?next=%2Fevent%2Fstream')

user_input = driver.find_element_by_name('username')
user_input.send_keys('example@example.com\t')
user_input.send_keys('password\n')
