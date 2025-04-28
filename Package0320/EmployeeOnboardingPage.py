import time
import datetime
import json
import logging
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

class EmployeeOnboardingPage():

    #【雇员入职】按钮
    addEMP_button_xpath = "//span[text()=' 雇员入职 ']"

    #【查询】按钮
    query_button_xpath = "//span[text()='查询']"

    #【选择客户组织】按钮
    selectOrg_button_xpath = "//*[@id='customer']/div[1]/h4/div[2]/div[1]/button"

    #【客户组织编码】标题
    org_code_xpath = "//label[text()='客户组织编码']"

    #【客户组织编码】输入框
    org_input_xpath = "./following-sibling::div//input[@class='el-input__inner' and @placeholder='请输入']"

    #【选择】按钮
    select_button_xpath = "//span[@class='el-link__inner' and text()='选择']"

    #【确认】按钮
    confirm_button_xpath = "//button[@class='el-button el-button--primary el-button--default']/span[text()=' 确认 ']"

    #【请输入】输入框
    please_input_xpath = "./following-sibling::div//input[@class='el-input__inner' and @placeholder='请输入']"

    #【雇员信息】标题
    employee_info_id = "employee"

    #【查看更多】
    more_info_xpath = "//span[@class='el-link__inner' and text()='查看更多']"

    # 【证件号】标题
    id_title_xpath = "//label[text()='证件号']"


    # 【姓名】标题
    name_xpath = "//label[text()='姓名']"

    # 【姓名】输入框
    name_input_xpath = please_input_xpath

    # 【手机号】标题
    phone_xpath = "//label[text()='手机号']"

    # 【手机号】输入框
    phone_xpath_input = please_input_xpath

    # 【邮箱】标题
    email_xpath = "//label[text()='邮箱']"
    # 【邮箱】输入框
    email_input_xpath = please_input_xpath


    # 【户籍地址邮编】标题
    domicile_address_id_xpath = "//label[text()='户籍地址邮编']"

    # 【户籍地址邮编】输入框
    domicile_address_id_input_xpath = please_input_xpath


    # 【户籍详细地址】标题
    domicile_address_xpath = "//label[text()='户籍地址-详细地址']"

    # 【户籍详细地址】输入框
    domicile_address_input_xpath = please_input_xpath


    # 【联系/居住地址详细地址】标题
    residential_address_xpath = "//label[text()='联系/居住地址-详细地址']"

    # 【联系/居住地址详细地址】输入框
    residential_address_input_xpath = please_input_xpath

    # 【居住地址邮编】标题
    residential_address_id_xpath = "//label[text()='居住地邮编']"

    # 【居住地址邮编】输入框
    residential_address_id_input_xpath = please_input_xpath

    # 【选择组合报价单】按钮
    select_quote_xpath = "//*[@id='quoation']/div[1]/h4/div[2]/div[1]/button/span"

    # 【组合报价单编号】标题
    quote_xpath = "//label[text()='组合报价单号']"

    # 【组合报价单编号】输入框
    quote_input_xpath = please_input_xpath

    # 【社保类服务参数工资】标题
    social_salary_classname = "el-input__inner"

    # 【社保类服务参数工资】输入框
    social_salary_input_xpath = ""

    # 【公积金类服务参数工资】标题
    house_salary_xpath = ""

    # 【公积金类服务参数工资】输入框
    house_salary_input_xpath = ""

    # 【证件号】输入框
    id_input_xpath = please_input_xpath

    # 【请选择】下拉
    dropdown_classname="el-select"

    #【文化程度】下拉选择
    education_level_xpath = "//span[text()='大学本科']"

    #【民族】下拉选择
    ethnic_xpath = "//span[text()='汉族']"

    #【政治面貌】下拉选择
    party_xpath = "//span[text()='群众']"

    #【婚姻状态】下拉选择
    marriage_xpath = "//span[text()='未婚']"

    #【户籍地址邮编】标题
    domicile_address_id_xpath = "//label[text()='户籍地址邮编']"

    #【户籍地址邮编】输入框
    domicile_address_id_input_xpath = please_input_xpath

    #地址下拉框
    address_dropdown_cssselector =  "input.el-input__inner[readonly][placeholder='请选择']"

    #户籍地址-省
    domicile_address_province_xpath =  "//span[text()='河北省']"

    #户籍地址-市
    domicile_address_city_xpath =  "//span[text()='秦皇岛市']"

    #户籍地址-区
    domicile_address_district_xpath =  "//span[text()='海港区']"

    #居住/联系地址下拉选项panel
    residential_address_panels_classname = "el-cascader-panel"

    # 居住/联系地址-省
    residential_address_province_xpath = "//span[text()='山西省']"

    # 居住/联系地址-市
    residential_address_city_xpath = "//span[text()='太原市']"

    # 居住/联系地址-区
    residential_address_district_xpath = "//span[text()='迎泽区']"

    # 构造函数，使用者需要关联浏览器对象（webdriver）
    def __init__(self, webdriver):
        self.driver = webdriver

    # 公共方法： 雇员花名册列表页面，点击【雇员入职】按钮
    def pressAddEmployeeButton(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.addEMP_button_xpath).click()

    # 公共方法： 雇员入职页面，点击【选择客户组织】按钮
    def pressSelectOrgButton(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.selectOrg_button_xpath).click()

    # 公共方法：选择客户组织弹窗页面，输入客户组织编号
    def enterOrgCode(self, OrgCode):
        self.driver.implicitly_wait(10)
        org = self.driver.find_element(By.XPATH, self.org_code_xpath)
        org.find_element(By.XPATH,self.org_input_xpath).send_keys(OrgCode)

    # 公共方法：点击【查询】按钮
    def pressQueryButton(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.query_button_xpath).click()

    # 公共方法：点击【选择】按钮
    def pressSelectButton(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.select_button_xpath).click()

    # 公共方法：点击【确认】按钮
    def pressConfirmButton(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.confirm_button_xpath).click()

    #公共方法：点击【查看更多】按钮
    def pressMoreInfoButton(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.more_info_xpath).click()

    #公共方法：输入雇员证件号
    def EnterID(self,ID_Code):
        self.driver.implicitly_wait(10)
        employee_param = self.driver.find_element(By.ID, self.employee_info_id)
        id_code = employee_param.find_element(By.XPATH, self.id_title_xpath)
        id_code.find_element(By.XPATH, self.id_input_xpath).send_keys(ID_Code)
        self.driver.switch_to.active_element.send_keys(Keys.TAB)

    #公共方法：输入雇员姓名
    def EnterName(self,Name):
        self.driver.implicitly_wait(10)
        name = self.driver.find_element(By.XPATH, self.name_xpath)
        name.find_element(By.XPATH, self.name_input_xpath).send_keys(Name)


    #公共方法：输入雇员手机号
    def EnterPhone(self,Phone):
        self.driver.implicitly_wait(10)
        phone = self.driver.find_element(By.XPATH, self.phone_xpath)
        phone.find_element(By.XPATH, self.phone_xpath_input).send_keys(Phone)

    #公共方法：输入邮箱
    def EnterEmail(self,Email):
        self.driver.implicitly_wait(10)
        email = self.driver.find_element(By.XPATH, self.email_xpath)
        email.find_element(By.XPATH, self.phone_xpath_input).send_keys(Email)

    #公共方法：选择文化程度
    def SelectEduLevel(self):
        self.driver.implicitly_wait(10)
        onboarding_selects = self.driver.find_elements(By.CLASS_NAME, self.dropdown_classname)
        onboarding_selects[8].click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.education_level_xpath).click()

    #公共方法：选择民族
    def SelectEthnic(self):
        self.driver.implicitly_wait(10)
        onboarding_selects = self.driver.find_elements(By.CLASS_NAME, self.dropdown_classname)
        onboarding_selects[9].click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.ethnic_xpath).click()

    #公共方法：选择政治面貌
    def SelectParty(self):
        self.driver.implicitly_wait(10)
        onboarding_selects = self.driver.find_elements(By.CLASS_NAME, self.dropdown_classname)
        onboarding_selects[10].click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.party_xpath).click()

    #公共方法：选择婚姻状态
    def SelectMarriage(self):
        self.driver.implicitly_wait(10)
        onboarding_selects = self.driver.find_elements(By.CLASS_NAME, self.dropdown_classname)
        onboarding_selects[11].click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.marriage_xpath).click()

    #公共方法：输入户籍地址邮编
    def EnterDomicileAddressId(self,DomicileAddressId):
        self.driver.implicitly_wait(10)
        domicile_address_id = self.driver.find_element(By.XPATH, self.domicile_address_id_xpath)
        domicile_address_id.find_element(By.XPATH, self.domicile_address_id_input_xpath).send_keys(DomicileAddressId)

    #公共方法：选择户籍地址 联系/居住地址 -省市区(县)
    def SelectDomicileAddress(self):
        self.driver.implicitly_wait(10)
        employee_param = self.driver.find_element(By.ID, self.employee_info_id)
        address_selects = employee_param.find_elements(By.CSS_SELECTOR, self.address_dropdown_cssselector)
        address_selects[0].click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.domicile_address_province_xpath).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.domicile_address_city_xpath).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.domicile_address_district_xpath).click()
        time.sleep(0.5)
        address_selects[1].click()
        time.sleep(0.5)
        panels = self.driver.find_elements(By.CLASS_NAME, self.residential_address_panels_classname)
        panel = panels[0]
        provinces = panel.find_elements(By.XPATH, self.residential_address_province_xpath)
        provinces[1].click()
        time.sleep(0.5)
        panel.find_element(By.XPATH, self.residential_address_city_xpath).click()
        time.sleep(0.5)
        panel.find_element(By.XPATH, self.residential_address_district_xpath).click()
        time.sleep(0.5)


    #公共方法：输入户籍详细地址
    def EnterDomicileAddress(self, DomicileAddress):
        self.driver.implicitly_wait(10)
        domicile_address = self.driver.find_element(By.XPATH, self.domicile_address_xpath)
        domicile_address.find_element(By.XPATH, self.domicile_address_input_xpath).send_keys(DomicileAddress)

    #公共方法：输入联系/居住地址详细地址
    def EnterResidentialAddress(self, ResidentialAddress):
        self.driver.implicitly_wait(10)
        residential_address = self.driver.find_element(By.XPATH, self.residential_address_xpath)
        residential_address.find_element(By.XPATH, self.residential_address_input_xpath).send_keys(ResidentialAddress)

    #公共方法：输入居住地址邮编
    def EnterResidentialAddressID(self, ResidentialAddressID):
        self.driver.implicitly_wait(10)
        residential_address_id = self.driver.find_element(By.XPATH, self.residential_address_id_xpath)
        residential_address_id.find_element(By.XPATH, self.residential_address_id_input_xpath).send_keys(ResidentialAddressID)
        self.driver.switch_to.active_element.send_keys(Keys.TAB)

    #公共方法：选择组合报价单
    def pressQuote(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.select_quote_xpath).click()

    #公共方法：输入组合报价单编号
    def EnterQuote(self, Quote):
        self.driver.implicitly_wait(10)
        quote = self.driver.find_element(By.XPATH, self.quote_xpath)
        quote.find_element(By.XPATH, self.quote_input_xpath)

    #公共方法：输入社保类服务参数工
    def EnterSocialSalary(self, SocialSalary):
        self.driver.implicitly_wait(10)
        social_salary = self.driver.find_element(By.CLASS_NAME, self.social_salary_classname)
        social_salary.find_element(By.XPATH, self.social_salary_input_xpath)
    #公共方法：选择合同签订方式

    #公共方法：输入公积金类服务参数工资
    def EnterHouseSalary(self, HouseSalary):
        self.driver.implicitly_wait(10)
        house_salary = self.driver.find_element(By.CLASS_NAME, self.house_salary_classname)
        house_salary.find_element(By.XPATH, self.house_salary_input_xpath)

    #公共方法：选择单位比例

    #公共方法：选择个人比例

    #公共方法：选择起缴年月（补充公积金）

    #公共方法：选择单位比例（补充公积金）

    #公共方法：选择个人比例（补充公积金）





    # 获取页面已关联的浏览器对象
    def getPageDriver(self):
        return self.driver
