# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException
# import time

    # def common_fn(self,select, index):
    #     config = configparser.ConfigParser()
    #     config.read('config.ini')
    #     obj = config.get('enum',index)
    #
    #     # 等待下拉框可点击
    #     dropdown = select[index]
    #     dropdown.click()
    #     # 等待选项出现并点击
    #     option_xpath = f"//span[text()='{obj}']"
    #     # option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
    #     option = self.driver.find_element(By.XPATH, option_xpath)
    #     option.click()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class WebAutomation:
    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def open_url(self, url):
        """打开指定URL"""
        self.driver.get(url)
        return self

    def find_element_by_label(self, label_text, timeout=10):
        # 先找到标签元素
        label_xpath = f'//label[text()="{label_text}"]'
        label_element = WebDriverWait(self, timeout).until(EC.presence_of_element_located((By.XPATH, label_xpath)))
        # 然后找到相邻的输入元素
        input_element = label_element.find_element(By.XPATH, './following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
        return input_element

if __name__ == "__main__":
    # 正确的使用方式
    automation = WebAutomation()  # 创建类的实例
    automation.open_url("https://sales-sit.ifsg.com.cn/sprt/login")  # 通过实例调用方法
    username = automation.driver.find_element(By.CSS_SELECTOR, "input.el-input__inner[type='text']")
    username.send_keys("00000")
    password = automation.driver.find_element(By.CSS_SELECTOR, "input.el-input__inner[type='password']")
    password.send_keys("00000")
    login_button = automation.driver.find_element(By.XPATH, "//button//span[text()='登录']")
    login_button.click()