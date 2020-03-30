# Need selenium to be able to open the browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass

comment_counter = 0
like_counter = 0
youtube_email_input = input("Enter your youtube email: ")
youtube_password_input = getpass.getpass("Enter your youtube password: ")
# Set the link to youtube
url = "https://www.youtube.com/"
# Set the browser. I run ubuntu so my default is firefox
driver = webdriver.Firefox()
# Open the link (instagram)
driver.get(url)
# Make it sleep so I can see what it is doing
time.sleep(5)
