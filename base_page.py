from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def webelement_text(self, locator, text):
        return Wait(self.driver, 5).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def webelement_click(self, locator):
        return Wait(self.driver, 5).until(EC.visibility_of_element_located(locator)).click()

    def webelement_clear(self, locator):
        return Wait(self.driver, 5).until(EC.visibility_of_element_located(locator)).send_keys(Keys.CLEAR)





