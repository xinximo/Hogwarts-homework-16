import yaml
from selenium.webdriver.common.by import By

from test_app_frame.base_page import BasePage


class Search(BasePage):
    def search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("xxxxx")
        self.load("../page/search.yaml")
        return True
