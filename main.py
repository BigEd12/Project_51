from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USER = YOUR-TWITTER-USERNAME
TWITTER_PASSWORD = YOUR-TWITTER-PASSWORD
CHROME_DRIVER_PATH = YOUR-CHROME-DRIVER-PATH
SPEEDTEST_URL = "https://www.speedtest.net/"
driver = webdriver.Chrome(CHROME_DRIVER_PATH)


def download_speeds():
    driver.get(SPEEDTEST_URL)
    time.sleep(5)
    privacy_accept = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[2]/div/div/button[2]')
    privacy_accept.click()

    time.sleep(10)
    start_test = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
    start_test.click()

    time.sleep(50)
    download_speed = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
    upload_speed = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    down_up_list = [download_speed.text, upload_speed.text]
    print(type(down_up_list))
    return down_up_list



def twitter_login():
    driver.get("https://twitter.com/")
    time.sleep(5)
    reject_cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/span/span')
    reject_cookies.click()

    time.sleep(2)
    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/div/span/span')
    login_button.click()

    try:
        time.sleep(5)
        notifications_off = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/span/span')
        notifications_off.click()
    except NoSuchElementException:
        pass

    time.sleep(3)
    phone_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    phone_field.send_keys(TWITTER_USER)
    phone_field.send_keys(Keys.ENTER)

    time.sleep(3)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password_field.send_keys(TWITTER_PASSWORD)
    password_field.send_keys(Keys.ENTER)

    time.sleep(10)
    tweet_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
    tweet_button.click()

    time.sleep(5)
    message = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    message.send_keys(f"@movistar_team\n¿Que esta pasando Movistar? Tengo bajadas de {download_speed}Mbps y subidas de {upload_speed}Mbps\n¿Cuando se termina la instalacion de fibra en ****************?")
    tweet = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
    tweet.click()

    time.sleep(5)
    driver.quit()

list = download_speeds()
download_speed = list[0]
upload_speed = list[1]
twitter_login()


