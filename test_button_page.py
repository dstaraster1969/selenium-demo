import pytest
from selenium import webdriver
from pages.button_page import ButtonPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@pytest.fixture()
def url():
    # the URL is hardcoded because it's not going to change
    return 'https://eviltester.github.io/synchole/buttons.html'


# @pytest.fixture()
# def button_page(driver):
#     return ButtonPage(driver)


def test_easy_to_sync_buttons(driver, url):  #, button_page):
    driver.get(url)
   # button_page.easy_button0.click()


