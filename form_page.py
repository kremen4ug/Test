import time

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):
    def fill_positive(self):
        product = 'Samsung'

        self.webelement_click(Locators.SEARCH_PRODUCT)
        self.webelement_text(Locators.SEARCH_PRODUCT, product)
        time.sleep(3)
        self.webelement_click(Locators.BUTTON_SEARCH)
        time.sleep(4)
        self.webelement_click(Locators.NEXT_PRODUCT)
        time.sleep(3)
        self.webelement_click(Locators.BUY)
        time.sleep(5)
        self.webelement_click(Locators.ORDER_FORM)
        time.sleep(5)
        self.webelement_click(Locators.LOGOS_ALLO)
        self.webelement_click(Locators.BASKET)
        time.sleep(3)
        self.webelement_click(Locators.DELETE_PRODUCT)
        time.sleep(3)
        self.webelement_click(Locators.CLOSE_WINDOW)
        time.sleep(3)

    def fill_negative(self):
        text_fill = '=-23%qaz'
        number_phone = "992331382"

        self.webelement_click(Locators.SEARCH_PRODUCT)
        self.webelement_text(Locators.SEARCH_PRODUCT, text_fill)
        time.sleep(3)
        self.webelement_click(Locators.BUTTON_SEARCH)
        time.sleep(3)
        self.webelement_click(Locators.AUTHORIZATION)
        self.webelement_click(Locators.NUMBER_CLICK)
        self.webelement_click(Locators.NUMBER_PHONE)
        self.webelement_text(Locators.NUMBER_PHONE, number_phone)
        time.sleep(3)
        self.webelement_click(Locators.NUMBER_CLICK)
        time.sleep(6)
        self.webelement_click(Locators.ANOTHER_METHOD)
        self.webelement_click(Locators.EMAIL_LOGIN)









