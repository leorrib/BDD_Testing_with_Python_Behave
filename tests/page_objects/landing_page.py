from selenium.webdriver.common.by import By

class LandingPage():
    def __init__(self, browser):
        self.browser = browser

    search_box = (By.ID, 'search_query_top')
    search_btn = (By.CSS_SELECTOR, "button[class*='search']")

    def _type_item_name(self, item):
        self.browser.find_element(*self.search_box).send_keys(item)

    def _click_search_btn(self):
        self.browser.find_element(*self.search_btn).click()

    def search_for_item(self, item):
        self._type_item_name(item)
        self._click_search_btn()
