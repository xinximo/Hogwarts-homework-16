# Generated by Selenium IDE
import pytest
import time
import json

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from faker import Faker


class TestWework:
    def setup_class(self):
        fake = Faker()
        self.ran_id = random.randint(0, 999999)
        self.ran_name = random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()', 5)
        self.name = fake.name()
        self.ram_telnum = random.randint(0, 99999999)

    def setup_method(self, method):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9927'  # 设置debug地址 # chrome --remote-debugging-port=9927
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_id("menu_contacts").click()
        cookie = driver.get_cookies()
        with open("data_cookie.yml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)

    def teardown_method(self, method):
        pass

    # @pytest.mark.run(order=1)
    # def test_get_cookie(self):
    #   opt = webdriver.ChromeOptions()
    #   opt.debugger_address = '127.0.0.1:9927'  # 设置debug地址
    #   driver = webdriver.Chrome(options=opt)
    #   driver.implicitly_wait(5)
    #   driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #   driver.find_element_by_id("menu_contacts").click()
    #   cookie=driver.get_cookies()
    #   with open("data_cookie.yml","w",encoding="UTF-8") as f:
    #     yaml.dump(cookie,f)

    @pytest.mark.run(order=1)
    def test_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("data_cookie.yml", "r", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.implicitly_wait(5)
        driver.find_element_by_id("menu_contacts").click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '[class="js_operationBar_footer ww_operationBar"] a:nth-child(2)')))
        driver.find_element_by_css_selector('[class="js_operationBar_footer ww_operationBar"] a:nth-child(2)').click()
        driver.implicitly_wait(5)
        driver.find_element_by_id('username').send_keys(self.name)
        driver.find_element_by_id('memberAdd_acctid').send_keys(f"wx{self.ran_id}")
        driver.find_element_by_css_selector('[class="ww_telInput"]> input:nth-child(2)').send_keys(
            f"130{self.ram_telnum}")
        driver.find_element_by_css_selector('[class="js_member_editor_form"]>div:nth-child(3)>a:nth-child(2)').click()
        driver.implicitly_wait(5)
        response = driver.find_element(By.CSS_SELECTOR, '[title="{}"]'.format(self.name)).text
        assert response == self.name
        # driver.find_element_by_xpath('//*[@class="js_member_editor_form"]/div[1]/a[2]').click()
        driver.quit()
