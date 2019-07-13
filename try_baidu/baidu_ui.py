from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.select import Select
import unittest


class baidu_ui_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = "https://www.baidu.com/"
        cls.dr = webdriver.Firefox()
        cls.dr.get(cls.url)
        cls.dr.implicitly_wait(10)

    def test_baiduset(self):
        # 鼠标移动的操作
        self.shezhi_link = self.dr.find_element_by_link_text("设置")
        ActionChains(self.dr).move_to_element(self.shezhi_link).perform()
        # 鼠标移动到设置栏位，并定位到“搜索设置”链接
        self.dr.find_element_by_link_text("搜索设置").click()
        sleep(3)
        # 选择搜索框提示不显示
        self.dr.find_element_by_xpath("//td[@id='se-settting-1']/input[2]").click()
        # 设置搜索语言范围
        self.dr.find_element_by_css_selector("td[id='se-settting-2']>input:nth-child(3)").click()
        # 设置搜索结果显示条数
        self.showdata = self.dr.find_element_by_css_selector("#nr")
        Select(self.showdata).select_by_value("20")
        # 设置搜索历史记录
        self.dr.find_element_by_css_selector("td[id='se-setting-5']>input:nth-child(3)").click()
        # 点击“保存设置”按钮
        self.dr.find_element_by_css_selector("#gxszButton").click()


    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.dr.quit()

if __name__ == "__main__":
    unittest.main()











