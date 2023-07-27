import pytest
from selenium import webdriver

from pages.form_page import FormPage


# These tests are far from exhaustive. This is an example of how I'd test this page.
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://eviltester.github.io/synchole/form.html')
    yield driver
    driver.close()


@pytest.fixture
def form_page(driver):
    return FormPage(driver)


def test_submit_form(form_page):
    username = 'Buffy Summers'
    form_page.enter_username(username)
    form_page.click_submit_button()

    assert 'Thanks' in form_page.get_submission_text()


def test_clear_form(form_page):
    form_page.enter_username('Willow Rosenberg')
    form_page.click_cancel_button()

    assert form_page.get_username() == ''


def test_username_confirmation(form_page):
    first_name = 'Xander'
    last_name = 'Harris'
    form_page.enter_username(f'{first_name} {last_name}')
    form_page.click_submit_button()

    confirmation = form_page.get_username_confirmation()
    assert f'{first_name}+{last_name}' in confirmation


def test_submit_confirmation(form_page):
    form_page.enter_username('Rupert Giles')
    form_page.click_submit_button()

    confirmation = form_page.get_submit_button_confirmation()
    assert 'submit' in confirmation

