# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class record(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_record(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        if not wd.find_element_by_id("2").is_selected():
            wd.find_element_by_id("2").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
