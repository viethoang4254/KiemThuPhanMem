from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    REMOVE_BTN = (By.XPATH, "//button[text()='Remove']")

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def get_cart_count(self):
        try:
            return int(self.get_text(self.CART_BADGE))
        except:
            return 0

    def open_cart(self):
        self.click(self.CART_LINK)

    def add_product_by_index(self, index=0):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        buttons[index].click()

    def remove_product_by_index(self, index=0):
        buttons = self.driver.find_elements(*self.REMOVE_BTN)
        if buttons:
            buttons[index].click()

    def sort_by(self, value):
        # value: az, za, lohi, hilo
        self.click(self.SORT_DROPDOWN)
        option = (By.XPATH, f"//option[@value='{value}']")
        self.click(option)

    def get_all_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAME)
        return [el.text for el in elements]

    def get_all_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICE)
        return [float(el.text.replace("$", "")) for el in elements]