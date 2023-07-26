from selenium.webdriver.common.by import By


class ButtonPage:
    def __init__(self, driver):
        self.driver = driver
        easy001_button = self.driver.find_element(By.ID, 'easy00')

