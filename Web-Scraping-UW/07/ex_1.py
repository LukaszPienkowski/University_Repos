from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
import datetime

# Init:
gecko_path = '/usr/local/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, service=ser)

url = 'http://campuswire.com/signin'
script = '/mnt/c/Users/lukas/ex_1.py'

# Actual program:
driver.get(url)

time.sleep(2)

username = driver.find_element(By.XPATH, '//input[@placeholder="Email"]')
my_email = input('Please provide your email:')
username.send_keys(my_email)

time.sleep(2)

password = driver.find_element(By.XPATH, '//input[@placeholder="password"]')
my_pass = getpass.getpass('Please provide your password:')
password.send_keys(my_pass)

time.sleep(2)

button = driver.find_element(By.XPATH, '//button[@type="submit"]')
button.click()

time.sleep(5)

chat = driver.find_element(By.XPATH, '/html/body/div[1]/div/aside[1]/div/div[1]/ul/li[2]/button')
chat.click()

time.sleep(2)

bot_test_chat = driver.find_element(By.XPATH, '//h5[. = "Przemek Kurek"]')
bot_test_chat.click()

time.sleep(2)

driver.find_element(By.XPATH, '//input[@type = "file"]').send_keys(script)

driver.quit()