# Need selenium to be able to open the browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass


##youtube_email_input = input("Enter your youtube email: ")
##youtube_password_input = getpass.getpass("Enter your youtube password: ")
youtube_email_input = "xxcuterootxx@gmail.com"
youtube_password_input = "SamsStreamBiz420"
youtube_search_topic = input("Enter your youtube topic: ")
# Set the link to youtube
url = "https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
# Set the browser. I run ubuntu so my default is firefox
driver = webdriver.Firefox()
# Open the link (instagram)
driver.get(url)
# Make it sleep so I can see what it is doing
time.sleep(5)
# Send Email Information
email = driver.find_elements_by_xpath('//*[@id="identifierId"]') 
email[0].send_keys(youtube_email_input)
#Click Next Button
youtube_login_next = driver.find_elements_by_xpath('//*[@id="identifierNext"]')[0].click()
time.sleep(3)
#Send Password Information
try: 
	password = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
	password[0].send_keys(youtube_password_input)
except:
	password = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
	youtube_password_input = getpass.getpass("Enter your youtube password: ")
	password[0].send_keys(youtube_password_input)

#Click Next
youtube_login_next = driver.find_elements_by_xpath('//*[@id="passwordNext"]')[0].click()
time.sleep(5)
#Enter the search topic

##for letter in youtube_search_topic:
##	if letter == ' ':
##		letter="+"

#Search the topic
driver.get("https://www.youtube.com/results?search_query=" + youtube_search_topic)
#Give Some Time To Load
time.sleep(5)
#Click the first video
click_video = driver.find_elements_by_xpath('//*[@id="video-title"]')[0].click()
##Wait Again
time.sleep(3)
##Scroll Down
driver.execute_script("window.scrollTo(0, 1080)")
##Wait Again
time.sleep(5)
##Scroll Down
driver.execute_script("window.scrollTo(0, 1500)")
##Wait Again
time.sleep(5)
##Click Comment
click_comment = driver.find_elements_by_xpath('//*[@id="contenteditable-root"]')[0].click()