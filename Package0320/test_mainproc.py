import sys
sys.path.append(r"C:\Users\d.a.xiao\PycharmProjects\pythonProject\Package0320")
import LoginPage
from Package0320 import EmployeeOnboardingPage
import tdata4EmployeeOnboarding
import time
import logging
from selenium import webdriver


class TestAssign():
    def setup_method(self, method):
        # 在每个测试方法前执行
        self.driver = webdriver.Chrome()  # 或其他浏览器驱动
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        # 在每个测试方法后执行
        self.driver.quit()

    def test_EmployeeOnboarding(self):
        logging.info("测试用例：用户登录----------开始")

        # 浏览器最大化
        self.driver.maximize_window()
        time.sleep(1)

        # 浏览器打开登录起始页
        self.driver.get(tdata4EmployeeOnboarding.LoginPage_url)
        time.sleep(1)

        # 建立登录页可操作对象
        myLoginPage = LoginPage.LoginPage(self.driver)
        time.sleep(1)

        # 登录操作
        myLoginPage.enterUsername(tdata4EmployeeOnboarding.LoginUserName)
        time.sleep(1)

        myLoginPage.enterPassword(tdata4EmployeeOnboarding.LoginPassWord)
        time.sleep(1)

        myLoginPage.pressLoginButton()
        time.sleep(1)

        logging.info("用户登录----------完成")
        time.sleep(3)

        #打开雇员花名册页面
        self.driver.get(tdata4EmployeeOnboarding.EmployeeRoster_url)
        logging.info("雇员花名册页面----------完成")

        myEMP = EmployeeOnboardingPage.EmployeeOnboardingPage(self.driver)
        time.sleep(3)

        #点击雇员入职按钮
        myEMP.pressAddEmployeeButton()
        time.sleep(3)

        #点击选择客户组织按钮
        myEMP.pressSelectOrgButton()
        time.sleep(2)

        #输入客户组织
        myEMP.enterOrgCode(tdata4EmployeeOnboarding.str_Org)
        time.sleep(2)

        #查询
        myEMP.pressQueryButton()
        time.sleep(2)

        #选择客户组织
        myEMP.pressSelectButton()
        time.sleep(2)

        #确认
        myEMP.pressConfirmButton()
        time.sleep(5)

        #点击查看更多
        myEMP.pressMoreInfoButton()

        #输入证件号
        myEMP.EnterID(tdata4EmployeeOnboarding.ID_Code)
        time.sleep(2)

        #输入姓名
        myEMP.EnterName(tdata4EmployeeOnboarding.Name)
        time.sleep(1)

        #输入手机号
        myEMP.EnterPhone(tdata4EmployeeOnboarding.Phone)
        time.sleep(1)

        #输入邮箱
        myEMP.EnterEmail(tdata4EmployeeOnboarding.Email)
        time.sleep(1)

        #选择文化程度
        myEMP.SelectEduLevel()
        time.sleep(1)

        #选择民族
        myEMP.SelectEthnic()
        time.sleep(1)

        #选择政治面貌
        myEMP.SelectParty()
        time.sleep(1)

        #选择婚姻状态
        myEMP.SelectMarriage()
        time.sleep(1)

        #输入户籍地址邮编
        myEMP.EnterDomicileAddressId((tdata4EmployeeOnboarding.DomicileAddressId))
        time.sleep(1)

        # 选择户籍地址 居住/联系 省市区县
        myEMP.SelectDomicileAddress()
        time.sleep(1)

        #输入户籍详细地址
        myEMP.EnterDomicileAddress(tdata4EmployeeOnboarding.DomicileAddress)
        time.sleep(1)

        #输入联系/居住地址详细地址
        myEMP.EnterResidentialAddress(tdata4EmployeeOnboarding.ResidentialAddress)
        time.sleep(1)

        #输入居住地址邮编
        myEMP.EnterResidentialAddressID(tdata4EmployeeOnboarding.ResidentialAddressID)
        time.sleep(2)

        #点击选择组合报价单按钮
        myEMP.pressQuote()
        time.sleep(3)

        #输入组合报价单号
        myEMP.EnterQuote(tdata4EmployeeOnboarding.quote_code)

        #查询组合报价单
        myEMP.pressQueryButton()

        #选择组合报价单
        myEMP.pressSelectButton()

        #确认
        myEMP.pressConfirmButton()