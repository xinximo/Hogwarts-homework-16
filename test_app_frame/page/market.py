import yaml
from selenium.webdriver.common.by import By

from test_app_frame.base_page import BasePage
from test_app_frame.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find_and_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        self.load("../page/market.yaml")
        return Search(self.driver)
