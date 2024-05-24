from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

PROMISED_DOWN = 150 #EnterYourDownSpeedLimit
PROMISED_UP = 150 #EnterYourUpSpeedLimit


class InternetSpeedTwitterBot:
    def __init__(self, twitter_handle):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = None
        self.up = None
        self.twitter_handle = twitter_handle

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        time.sleep(60)

        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

    def tweet_at_provider(self):
        if float(self.down) < PROMISED_DOWN or float(self.up) < PROMISED_UP:
            self.driver.get("https://x.com/login")

            sign_in_element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Sign in')]"))
            )
            sign_in_element.click()

            username_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            username_field.send_keys("Enter Your Username", Keys.RETURN)

            try:
                password_field = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )
                password_field.send_keys("Enter Your Password", Keys.RETURN)

            except TimeoutException:
                username_field_2 = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]'))
                )
                username_field_2.send_keys('Enter Your Username', Keys.RETURN)

                password_field = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )
                password_field.send_keys("Enter Your Password", Keys.RETURN)

                time.sleep(10)

            tweet_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']")))

            tweet_box.send_keys(f"@{self.twitter_handle} My internet speed is too slow, here is what I'm getting "
                                f"Download Speed: {self.down}Mbps, Upload Speed: {self.up}Mbps. Which isn't "
                                f"your guaranteed speed")

            post_button_xpath = "//div[contains(@class, 'css-175oi2r') and contains(@class, 'r-sdzlij') and contains(@class, 'r-1phboty') and contains(@class, 'r-rs99b7') and contains(@class, 'r-lrvibr') and contains(@class, 'r-1cwvpvk') and contains(@class, 'r-2yi16') and contains(@class, 'r-1qi8awa') and contains(@class, 'r-3pj75a') and contains(@class, 'r-o7ynqc') and contains(@class, 'r-6416eg') and contains(@class, 'r-icoktb') and contains(@class, 'r-1ny4l3l')]"

            try:
                post_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, post_button_xpath))
                )
                print("Post button found, clicking now...")
                post_button.click()
            except TimeoutException:
                print("Failed to find the post button.")

            time.sleep(10)

        else:
            self.driver.get("https://x.com/login")

            sign_in_element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Sign in')]"))
            )
            sign_in_element.click()

            username_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            username_field.send_keys("Enter Your username", Keys.RETURN)

            try:
                password_field = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )
                password_field.send_keys("Enter Your password", Keys.RETURN)

            except TimeoutException:
                username_field_2 = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]'))
                )
                username_field_2.send_keys('Enter your Username', Keys.RETURN)

                password_field = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )
                password_field.send_keys("Enter Your Password", Keys.RETURN)

                time.sleep(10)

            tweet_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']")))

            tweet_box.send_keys(f"@{self.twitter_handle} My internet speed is excellent today! "
                                f"Download Speed: {self.down}Mbps, Upload Speed: {self.up}Mbps. Keep up the good work!")

            post_button_xpath = "//div[contains(@class, 'css-175oi2r') and contains(@class, 'r-sdzlij') and contains(@class, 'r-1phboty') and contains(@class, 'r-rs99b7') and contains(@class, 'r-lrvibr') and contains(@class, 'r-1cwvpvk') and contains(@class, 'r-2yi16') and contains(@class, 'r-1qi8awa') and contains(@class, 'r-3pj75a') and contains(@class, 'r-o7ynqc') and contains(@class, 'r-6416eg') and contains(@class, 'r-icoktb') and contains(@class, 'r-1ny4l3l')]"

            try:
                post_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, post_button_xpath))
                )
                print("Post button found, clicking now...")
                post_button.click()
            except TimeoutException:
                print("Failed to find the post button.")
            time.sleep(10)


bot = InternetSpeedTwitterBot("Enter your internet provider handle")
bot.get_internet_speed()
print(f"Download Speed: {bot.down}Mbps")
print(f"Upload Speed: {bot.up}Mbps")
bot.tweet_at_provider()