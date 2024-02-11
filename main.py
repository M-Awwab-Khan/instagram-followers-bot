from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

MY_EMAIL = 'fakeofawwab@gmail.com'
MY_PASSWORD = '(^;E7JM_Rpfhhqy'
SIMILAR_ACCOUNT = 'learn.machinelearning'

class InstaFollower:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get('https://instagram.com/')
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(MY_EMAIL)
        self.driver.find_element(By.NAME, 'password').send_keys(MY_PASSWORD)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))).click()


    def find_followers(self):
        self.driver.get(f'https://instagram.com/{SIMILAR_ACCOUNT}/')
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a'))).click()
        followers_modal = wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]')))
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_modal)
            time.sleep(2)
    def follow(self):
        

if __name__ == '__main__':
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()