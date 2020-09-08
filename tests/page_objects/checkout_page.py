from selenium.webdriver.common.by import By

class CheckoutPage():
    def __init__(self, browser):
        self.browser = browser

    item_name_locator = "dynamic locator 1"
    color_locator = "dynamic locator 2"
    price_locator = "dynamic locator 3"
    quantity_locator = "dynamic locator 4"

    def _validate_item_name(self, item):
        self.item_name_locator = (By.XPATH, f"//td //a[text()[contains(.,'{item.capitalize()}')]]")
        displayed_name = self.browser.find_element(*self.item_name_locator).text
        assert item.lower() in displayed_name.lower()

    def _validate_color(self, item, color):
        self.color_locator = (By.XPATH, f"//td //a[text()[contains(.,'{item.capitalize()}')]]/../../small/a")
        displayed_color = self.browser.find_element(*self.color_locator).text
        assert color.lower() in displayed_color.lower()

    def _validate_price(self, item, price):
        self.price_locator = (By.XPATH, f"//a[text()[contains(.,'{item.capitalize()}')]]/../../following-sibling::td[2] //* //span")
        displayed_price = self.browser.find_element(*self.price_locator).text
        assert price == displayed_price

    def _validate_quantity(self, item, quantity):
        self.quantity_locator = (By.XPATH, f"//a[text()[contains(.,'{item.capitalize()}')]]/../../following-sibling::td[3] //input[1]")
        displayed_amount = self.browser.find_element(*self.quantity_locator).get_attribute("value")
        assert quantity == displayed_amount 

    def validate_result(self, item, color, price, quantity):
        self._validate_item_name(item)
        self._validate_color(item, color)
        self._validate_price(item, price)
        self._validate_quantity(item, quantity)