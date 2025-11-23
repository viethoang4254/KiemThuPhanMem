from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    def enter_information(self, first_name="", last_name="", zip_code=""):
        if first_name: self.type(self.FIRST_NAME, first_name)
        if last_name: self.type(self.LAST_NAME, last_name)
        if zip_code: self.type(self.ZIP_CODE, zip_code)
        self.click(self.CONTINUE_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR)