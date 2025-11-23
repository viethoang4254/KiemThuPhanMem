from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.credentials import *
import pytest
class TestSortProducts:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        LoginPage(driver).driver.get("https://www.saucedemo.com/")
        LoginPage(driver).login(VALID_USERNAME, VALID_PASSWORD)
        self.inventory = InventoryPage(driver)

    def test_sort_by_name_a_to_z(self):
        self.inventory.sort_by("az")
        names = self.inventory.get_all_product_names()
        assert names == sorted(names)

    def test_sort_by_price_low_to_high(self):
        self.inventory.sort_by("lohi")
        prices = self.inventory.get_all_product_prices()
        assert prices == sorted(prices)