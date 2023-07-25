class MyButton:
    def __init__(self, driver, search_type, search_string):
        self.element = driver.find_element(search_type, search_string)

    def click(self):
        self.element.click()
