from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# FormPage abstracts out the actions that can occur on the form page
class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        try:
            self.driver.find_element(By.NAME, 'username').send_keys(username)
        except NoSuchElementException:
            # if the element isn't found, do nothing. This will cause tests to fail.
            pass

    def get_username(self):
        try:
            return self.driver.find_element(By.NAME, 'username').text
        except NoSuchElementException:
            return None

    def click_cancel_button(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, '[value=cancel]').click()
        except NoSuchElementException:
            # if the cancel button isn't found, do nothing. This will cause tests to fail
            pass

    def click_submit_button(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, '[value=submit').click()
        except NoSuchElementException:
            pass

    def get_submission_text(self):
        try:
            return self.driver.find_element(By.ID, 'thanks').text
        except NoSuchElementException:
            return None

    def get_username_confirmation(self):
        # text_to_be_present_in_element() returns a bool
        # wait for the element to be present, then get its text
        # the locator is passed into EC as a tuple, but find_element takes string, string
        try:
            self.wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-name=username]'), 'username'))
            return self.driver.find_element(By.CSS_SELECTOR, '[data-name=username]').text
        except NoSuchElementException:
            return None

    def get_submit_button_confirmation(self):
        try:
            self.wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-name=submitbutton]'), 'submit'))
            return self.driver.find_element(By.CSS_SELECTOR, '[data-name=submitbutton]').text
        except NoSuchElementException:
            return None

    def get_header_text(self):
        try:
            return self.driver.find_element(By.TAG_NAME, 'h1').text
        except NoSuchElementException:
            return None
