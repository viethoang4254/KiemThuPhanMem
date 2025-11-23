from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    SUCCESS_HEADER = (By.CLASS_NAME, "complete-header")

    def is_order_successful(self):
        return "Thank you for your order!" in self.get_text(self.SUCCESS_HEADER)