from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepTwoPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def click_finish(self):
        self.click(self.FINISH_BUTTON)