import pytest
from selenium import webdriver

from button_page import ButtonPage


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def test_easy_buttons(driver):
    driver.get('https://eviltester.github.io/synchole/buttons.html')

    button_page = ButtonPage(driver)

    button_page.click_easy_button_00()
    button_page.click_easy_button_01()
    button_page.click_easy_button_02()
    button_page.click_easy_button_03()

    assert button_page.easy_button_message_text() == 'All Buttons Clicked'
