from selenium import webdriver
from time import sleep

# url = "https://www.baidu.com"
# dr = webdriver.Firefox()
# dr.get(url)
# dr.find_element_by_css_selector(".s_ipt").clear()
# dr.find_element_by_css_selector(".s_ipt").send_keys("python")
# dr.find_element_by_css_selector(".bg.s_btn").click()
# sleep(3)
#
# dr.quit()

url1 = "http://ask.testfan.cn/"
dr = webdriver.Firefox()
dr.get(url1)
dr.find_elements_by_css_selector(".form-control")[0].clear()
dr.find_elements_by_css_selector(".form-control")[0].send_keys("pyhon")
dr.find_element_by_css_selector(".input-group-addon.btn").click()
sleep(3)
dr.quit()