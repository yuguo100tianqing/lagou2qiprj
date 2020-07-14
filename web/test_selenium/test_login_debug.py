import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_debug_login(self):
        option = Options()
        option.debugger_address = "localhost:9222/"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable
                                             ((By.CSS_SELECTOR, "#menu_index > span")))
        self.driver.find_element_by_css_selector("#menu_index > span").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable
                                             ((By.CSS_SELECTOR,
                                               "#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(2) > div > span.index_service_cnt_item_title")))
        self.driver.find_element_by_css_selector(
            "#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(2) > div > span.index_service_cnt_item_title").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located
                                             ((By.CSS_SELECTOR, "#js_upload_file_input")))
        self.driver.find_element_by_css_selector("#js_upload_file_input").send_keys("E:/00/111.xlsx")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located
                                             ((By.ID, "upload_file_name")))
        assert_ele = self.driver.find_element_by_id("upload_file_name").text
        print(assert_ele)
        assert assert_ele == "111.xlsx"


class TestCookies:
    def test_get_cookies(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        sleep(30)
        cookies = driver.get_cookies()
        try:
            with open("cookie.json", "w") as f:
                json.dump(cookies, f)
        except:
            print("打开文件失败")
            assert False
        driver.close()

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        pass
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable
                                             ((By.CSS_SELECTOR,
                                               "#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(2) > div > span.index_service_cnt_item_title")))
        self.driver.find_element_by_css_selector(
            "#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(2) > div > span.index_service_cnt_item_title").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located
                                             ((By.CSS_SELECTOR, "#js_upload_file_input")))
        self.driver.find_element_by_css_selector("#js_upload_file_input").send_keys("E:/00/111.xlsx")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located
                                             ((By.ID, "upload_file_name")))
        assert_ele = self.driver.find_element_by_id("upload_file_name").text
        print(assert_ele)
        assert assert_ele == "111.xlsx"
