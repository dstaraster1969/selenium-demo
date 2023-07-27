from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.driver.find_element(By.NAME, 'username').send_keys(username)

    def get_username(self):
        return self.driver.find_element(By.NAME, 'username').text

    def click_cancel_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[value=cancel]').click()

    def click_submit_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[value=submit').click()

    def get_submission_text(self):
        return self.driver.find_element(By.ID, 'thanks').text

    def get_username_confirmation(self):
        # text_to_be_present_in_element() returns a bool
        # wait for the element to be present, then get its text
        # the locator is passed into EC as a tuple, but find_element takes string, string
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-name=username]'), 'username'))

        return self.driver.find_element(By.CSS_SELECTOR, '[data-name=username]').text

    def get_submit_button_confirmation(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-name=submitbutton').text

