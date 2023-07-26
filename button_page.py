from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ButtonPage:
    def __init__(self, wait):
        self.wait = wait

    # easy_button_00 = (By.ID, 'easy00')
    def click_easy_button_00(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'easy00'))).click()

    def click_easy_button_01(self):
       self.wait.until(EC.element_to_be_clickable((By.ID, 'easy01'))).click()

    def click_easy_button_02(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'easy02'))).click()

    def click_easy_button_03(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'easy03'))).click()

    easy_button_message = (By.ID, 'easybuttonmessage')