from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot():

    def __init__(self):


            def download_speeds(self):
                    CHROME_DRIVER_PATH = "C:\Dev\chromedriver.exe"
                    SPEEDTEST_URL = "https://www.speedtest.net/"
                    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
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
                    down_up_list = [download_speed, upload_speed]
                    print(type(down_up_list))
                    return down_up_list
