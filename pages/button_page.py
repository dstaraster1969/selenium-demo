from selenium.webdriver.common.by import By
from test_widgets.my_button import MyButton


class ButtonPage:
    def __init__(self, driver):
        self.driver = driver
        search_type = By.ID
        id_string = 'easy00'
        self.easy_button0 = MyButton(self.driver, By.ID, id_string)

