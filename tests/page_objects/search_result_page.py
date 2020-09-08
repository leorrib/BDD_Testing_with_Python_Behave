from selenium.webdriver.common.by import By

class SearchResultPage():
    def __init__(self, browser):
        self.browser = browser

    search_result = (By.CSS_SELECTOR, "[class='product-container'] [class*='name']")
    item_img = "dynamic locator"
    alert = (By.CSS_SELECTOR, "[class*='alert']")

    def _validate_result(self, item):
        displayed_result = self.browser.find_element(*self.search_result).text
        assert item.lower() in displayed_result.lower()

    def _click_img(self, item):
        self.item_img = (By.CSS_SELECTOR, f"img[title*='{item.capitalize()}']")
        self.browser.find_element(*self.item_img).click()

    def check_result_and_click_item(self, item):
        self._validate_result(item)
        self._click_img(item)

    def validate_alert(self, message):
        alert_text = self.browser.find_element(*self.alert).text
        assert alert_text == message