
from pages.form_page import FormPage


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://allo.ua/')
        form_page.open()
        form_page.fill_positive()

    def test_negative(self, driver):
        form_page = FormPage(driver, 'https://allo.ua/')
        form_page.open()
        form_page.fill_negative()


