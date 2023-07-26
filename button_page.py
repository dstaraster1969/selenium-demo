from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # actions against elements in the Easy to Sync section of the page
    def click_easy_button_00(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'easy00'))).click()

    def click_easy_button_01(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'easy01'))).click()

    def click_easy_button_02(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'easy02'))).click()

    def click_easy_button_03(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'easy03'))).click()

    def easy_button_message_text(self):
        return self.driver.find_element(By.ID, 'easybuttonmessage').text

    # actions against elements in the Harder to Sync section of the page
    def click_hard_button_00(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button00'))).click()

    def click_hard_button_01(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button01'))).click()

    def click_hard_button_02(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button02'))).click()

    def click_hard_button_03(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button03'))).click()

    def hard_button_message_text(self):
        return self.driver.find_element(By.ID, 'buttonmessage').text

