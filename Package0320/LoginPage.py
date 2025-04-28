import logging
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):  # 这是正确的构造函数位置
        self.driver = driver
        # 页面元素定位器
        self.textbox_username_css_selector = "input.el-input__inner[type='text']"
        self.textbox_password_css_selector = "input.el-input__inner[type='password']"
        self.button_login_xpath = "//button//span[text()='登录']"

    def __clickLoginTextbox(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_css_selector).click()

    def __clickPasswordTextbox(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css_selector).click()

    def enterUsername(self, username):
        self.__clickLoginTextbox()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_css_selector).send_keys(username)
        logging.info("测试账号：" + str(username))

    def enterPassword(self, password):
        self.__clickPasswordTextbox()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css_selector).send_keys(password)

    def pressLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def getPageDriver(self):
        return self.driver