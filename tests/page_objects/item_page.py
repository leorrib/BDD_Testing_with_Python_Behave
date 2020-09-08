from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class ItemPage():
    def __init__(self, browser):
        self.browser = browser

    item_name = (By.CSS_SELECTOR, "[itemprop='name']")
    color = "dynamic locator"
    btn_add_to_cart = (By.CSS_SELECTOR, "p[id*='cart'] span")
    btn_checkout = (By.CSS_SELECTOR, "[title*='checkout'] span")

    def _validate_item_name(self, item):
        text = self.browser.find_element(*self.item_name).text
        assert item.lower() in text.lower()

    def _choose_color(self, color):
        self.color = (By.CSS_SELECTOR, f"li a[name='{color.capitalize()}']")
        action = ActionChains(self.browser)
        action.click(self.browser.find_element(*self.color)).perform()

    def check_name_and_pick_a_color(self, item, color):
        self._validate_item_name(item)
        self._choose_color(color)

    def _click_add_to_cart(self):
        self.browser.find_element(*self.btn_add_to_cart).click()

    def _select_checkout(self):
        self.browser.find_element(*self.btn_checkout).click()

    def add_to_cart_and_checkout(self):
        self._click_add_to_cart()
        self._select_checkout()


