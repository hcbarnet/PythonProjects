# Need selenium to be able to open the browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass

hashtag_counter = 5
like_counter = 0
facebook_email_input = input("Enter your Facebook email: ")
facebook_password_input = getpass.getpass("Enter your Facebook password: ")
# Set the link to instagram
url = "https://www.instagram.com/"
# Set the browser. I run ubuntu so my default is firefox
driver = webdriver.Firefox()
# Open the link (instagram)
driver.get(url)
# Make it sleep so I can see what it is doing
time.sleep(5)
# Click login with facebook
facebook_login_instagram = driver.find_elements_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]')[0].click()

facebook_email = driver.find_elements_by_xpath('//*[@id="email"]') 
facebook_email[0].send_keys(facebook_email_input)

facebook_password = driver.find_elements_by_xpath('//*[@id="pass"]')
facebook_password[0].send_keys(facebook_password_input)

facebook_login_facebook = driver.find_elements_by_xpath(
    '//*[@id="loginbutton"]')[0].click()
time.sleep(15)
turn_off_notifications = driver.find_elements_by_xpath(
    '/html/body/div[4]/div/div/div[3]/button[2]')[0].click()

while True:
    hashtags = [
        '#instagood',
        '#sexy',
        '#pink',
        '#weekend',
        '#boy',
        '#photography',
        '#picoftheday',
        '#health',
        '#Home',
        '#live',
        '#like4like',
        '#igers',
        '#amazing',
        '#awesome',
        '#model',
        '#entrepreneur',
        '#work',
        '#nice',
        '#instadaily',
        '#drawing',
        '#Halloween',
        '#hair',
        '#vsco',
        '#explore',
        '#newyork',
        '#sunset',
        '#wanderlust',
        '#Japan',
        '#goals',
        '#gym',
        '#color',
        '#bodybuilding',
        '#ootd',
        '#likeforlike',
        '#follow',
        '#holiday',
        '#vintage',
        '#followme',
        '#lol',
        '#night',
        '#portrait',
        '#music',
        '#art',
        '#photoshoot',
        '#fit',
        '#happy',
        '#sweet',
        '#pretty',
        '#landscape',
        '#bestoftheday',
        '#cute',
        '#fashionblogger',
        '#flowers',
        '#foodie',
        '#l4l',
        '#nofilter',
        '#girl',
        '#makeup',
        '#healthy',
        '#inspiration',
        '#funny',
        '#instapic',
        '#italy',
        '#Repost',
        '#look',
        '#instalike',
        '#fall',
        '#architecture',
        '#instafashion',
        '#City',
        '#food',
        '#Selfie',
        '#beauty',
        '#training',
        '#canon',
        '#adventure',
        '#fashion',
        '#red',
        '#Family',
        '#cool',
        '#trip',
        '#sun',
        '#fitness',
        '#photo',
        '#luxury',
        '#dog',
        '#wedding',
        '#sky',
        '#USA',
        '#swag',
        '#motivation',
        '#summer',
        '#TBT',
        '#lifestyle',
        '#vscocam',
        '#party',
        '#artist',
        '#paris',
        '#insta',
        '#quotes']

    instagram_search_bar = driver.find_elements_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    instagram_search_bar[0].send_keys(str(hashtags[hashtag_counter]))
    hashtag_counter = hashtag_counter + 1

    if hashtag_counter == 100:
        hashtag_counter = 0

    time.sleep(15)
    like_for_follow_search = driver.find_elements_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[1]/span')[0].click()

    time.sleep(15)

    try:
        most_recent_photo = driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/h2')
        ac = ActionChains(driver)
        time.sleep(15)
        driver.execute_script("window.scrollTo(0, 1000)")

    except BaseException:
        most_recent_photo = driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[1]/h2/div')
        ac = ActionChains(driver)
        time.sleep(15)

    # move left 10 pixels, down 100.
    ac.move_to_element(most_recent_photo).move_by_offset(-10,
                                                         100).click().perform()
    time.sleep(15)
    x = 0
    while True:
        try:
            time.sleep(2)
            click_the_heart = driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]').click()
            time.sleep(2)
            click_right_arrow = driver.find_element_by_xpath(
                '/html/body/div[4]/div[1]/div/div/a[2]').click()
            time.sleep(2)
            x = x + 1
        except BaseException:
            x = 10

        if x == 10:
            # Set the link to instagram
            click_the_x = driver.find_element_by_xpath(
                '/html/body/div[4]/div[3]/button').click()
            break
