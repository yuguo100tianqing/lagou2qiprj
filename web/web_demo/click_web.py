from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select


class ClickWeb:
    def __init__(self):
        self.CMun = 'CMCCAdmin'
        self.CMpd = 'aDm8H%MdA'
        self.CMaddr = "http://192.168.1.1"
        self.driver = webdriver.Chrome()
        self.driver.get(self.CMaddr)
        self.driver.implicitly_wait(15)

    def RepeatClick(self):
        self.driver.find_element_by_css_selector("#user_name").clear()
        self.driver.find_element_by_css_selector("#user_name").send_keys(self.CMun)
        self.driver.find_element_by_css_selector("#password").clear()
        self.driver.find_element_by_css_selector("#password").send_keys(self.CMpd)
        self.driver.find_element_by_css_selector("#login_btn").click()
        self.driver.find_element_by_css_selector("#first_menu_network").click()
        self.driver.find_element_by_css_selector("#sub_second_menu_network_network_wifi").click()
        self.driver.find_element_by_css_selector("#sub_third_menu_network_network_wifi_network_wifi_base").click()
        self.driver.switch_to.frame("network_iframe")
        selector = Select(self.driver.find_element_by_id("secondaryChannel"))
        for i in range(1, 500):
            selector.select_by_index(i % 2)
            self.driver.find_element_by_css_selector("#apply").click()
            print(i)
            sleep(2)
        pass

        self.driver.close()


if __name__ == '__main__':
    clickweb = ClickWeb()
    clickweb.RepeatClick()
