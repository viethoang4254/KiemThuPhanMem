import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.credentials import *

class TestAddToCart:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        LoginPage(driver).driver.get("https://www.saucedemo.com/")
        LoginPage(driver).login(VALID_USERNAME, VALID_PASSWORD)
        self.inventory = InventoryPage(driver)
        self.cart = CartPage(driver)

    def test_add_single_product_to_cart(self):
        initial_count = self.inventory.get_cart_count()
        self.inventory.add_product_by_index(0)
        assert self.inventory.get_cart_count() == initial_count + 1

        self.inventory.open_cart()
        assert self.cart.get_cart_item_count() == 1

    def test_add_multiple_products_to_cart(self):
        self.inventory.add_product_by_index(0)
        self.inventory.add_product_by_index(1)
        self.inventory.add_product_by_index(2)
        assert self.inventory.get_cart_count() == 3