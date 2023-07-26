import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

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


def test_easy_to_sync_buttons(driver, url):
    driver.get(url)
    button_page = ButtonPage(driver)
    


