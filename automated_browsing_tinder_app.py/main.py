import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome('c:/Development/chromedriver.exe')

driver.get("https://tinder.com/app/recs")


# press Login
driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]').click()

# press Login with Facebook
time.sleep(2)
facebook_login = driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_login.click()

# SWITCHING SELENIUM TO THE NEW WINDOW

google_window = driver.window_handles[1]
driver.switch_to.window(google_window)


# enter the email and password
time.sleep(2)
my_email = os.environ['EMAIL']
my_password = os.environ['PASSWORD']
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(my_email)
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(my_password)

# click Login
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()

#   SWITCH TO THE ORIGIN WINDOW
origin_window = driver.window_handles[0]
driver.switch_to.window(origin_window)


# click Allow to allow tinder to access my location
time.sleep(10)
allow = driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div/div/div[3]/button[1]')
allow.click()

# click on NOT INTERESTED to skip notification
time.sleep(1)
discard = driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div/div/div[3]/button[2]')
discard.click()

# click accept, to accept cookies
time.sleep(1)
accept = driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[2]/div/div/div[1]/div[1]/button')
accept.click()

# click Nope
time.sleep(15)
nope = driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
for _ in range(0, 20):
    nope.click()
    time.sleep(2)