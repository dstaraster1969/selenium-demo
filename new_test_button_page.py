import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from button_page import ButtonPage


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def test_easy_buttons(driver):
    driver.get('https://eviltester.github.io/synchole/buttons.html')
    wait = WebDriverWait(driver, 10)

    button_page = ButtonPage()

    wait.until(EC.element_to_be_clickable(button_page.easy_button_00)).click()
    wait.until(EC.element_to_be_clickable(button_page.easy_button_01)).click()
    wait.until(EC.element_to_be_clickable(button_page.easy_button_02)).click()
    wait.until(EC.element_to_be_clickable(button_page.easy_button_03)).click()

    message_text = driver.find_element(By.ID, 'easybuttonmessage').text
    assert message_text == 'All Buttons Clicked'