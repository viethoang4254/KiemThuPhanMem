import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.credentials import *

class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        LoginPage(driver).driver.get("https://www.saucedemo.com/")
        LoginPage(driver).login(VALID_USERNAME, VALID_PASSWORD)
        self.inventory = InventoryPage(driver)
        self.cart = CartPage(driver)
        self.info = CheckoutStepOnePage(driver)
        self.overview = CheckoutStepTwoPage(driver)
        self.complete = CheckoutCompletePage(driver)

    def test_successful_checkout(self):
        self.inventory.add_product_by_index(0)
        self.inventory.open_cart()
        self.cart.click_checkout()

        self.info.enter_information("Nguyễn", "Văn A", "700000")
        self.overview.click_finish()

        assert self.complete.is_order_successful()

    def test_checkout_missing_first_name(self):
        self.inventory.add_product_by_index(0)
        self.cart.click_checkout()
        self.info.enter_information("", "Văn A", "700000")
        assert "First Name is required" in self.info.get_error_message()