import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.credentials import *

class TestRemoveFromCart:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        LoginPage(driver).driver.get("https://www.saucedemo.com/")
        LoginPage(driver).login(VALID_USERNAME, VALID_PASSWORD)
        self.inventory = InventoryPage(driver)

    def test_remove_from_inventory_page(self):
        self.inventory.add_product_by_index(0)
        self.inventory.remove_product_by_index(0)
        assert self.inventory.get_cart_count() == 0

    def test_remove_from_cart_page(self):
        self.inventory.add_product_by_index(0)
        self.inventory.open_cart()
        self.inventory.remove_product_by_index(0)
        assert self.inventory.get_cart_count() == 0