import pytest
from selenium import webdriver

from button_page import ButtonPage


# using function scope for fixtures because the page needs to be reloaded for each test
# (that resets everything
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://eviltester.github.io/synchole/buttons.html')
    yield driver
    driver.close()


@pytest.fixture
def button_page(driver):
    return ButtonPage(driver)


# the first time I tested against this page, the easy buttons came up immediately
# since then, there's been delays added, so only including here for completeness,
# but the two test are basically identical
def test_easy_buttons(driver, button_page):
    button_page.click_easy_button_00()
    button_page.click_easy_button_01()
    button_page.click_easy_button_02()
    button_page.click_easy_button_03()

    assert button_page.easy_button_message_text() == 'All Buttons Clicked'


def test_hard_buttons(driver, button_page):
    button_page.click_hard_button_00()
    button_page.click_hard_button_01()
    button_page.click_hard_button_02()
    button_page.click_hard_button_03()

    assert button_page.hard_button_message_text() == 'All Buttons Clicked'
