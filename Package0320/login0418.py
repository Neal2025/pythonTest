from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from employee_onboarding import WebAutomation

#chrome_options = Options()
#chrome_options.add_argument("--auto-open-devtools-for-tabs")  # 自动打开开发者工具
#driver = webdriver.Chrome(options=chrome_options)

try:
    # 打开目标页面
    #driver.get("https://sales-sit.ifsg.com.cn/sprt/login")
    automation = WebAutomation()  # 创建类的实例
    automation.open_url("https://sales-sit.ifsg.com.cn/sprt/login")  # 通过实例调用方法
    time.sleep(1)
    username = automation.driver.find_element(By.CSS_SELECTOR, "input.el-input__inner[type='text']")
    username.send_keys("00000000")
    password = automation.driver.find_element(By.CSS_SELECTOR, "input.el-input__inner[type='password']")
    password.send_keys("00000000")
    login_button = automation.driver.find_element(By.XPATH, "//button//span[text()='登录']")
    login_button.click()

finally:
    time.sleep(10)
    automation.driver.maximize_window()
    wait = WebDriverWait(automation.driver, 10)
    automation.driver.get("https://sales-sit.ifsg.com.cn/sprt/hrsassgin/employee/employeeRosterSearch")
    time.sleep(3)

    query = automation.driver.find_element(By.XPATH, "//span[text()='查询']")
    query.click()
    time.sleep(5)

    print("雇员入职")
    onboarding = automation.driver.find_element(By.XPATH, "//span[text()=' 雇员入职 ']")
    onboarding.click()
    time.sleep(5)

    org = automation.driver.find_element(By.XPATH, '//span[@class="" and contains(., "选择客户组织")]')
    org.click()
    time.sleep(3)
    print("选择客户组织")

    WebDriverWait(automation.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-dialog")))
    print("客户组织弹窗出现")

    # 1. 先定位到 label 元素
    action_chains = ActionChains(automation.driver)
    org = WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="客户组织编码"]')))

    # 2. 以 org (label) 为父级，向下查找 input
    org_code = org.find_element(By.XPATH, './following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
    org_code.send_keys("C000000269")
    query_button = automation.driver.find_element(By.XPATH, '//button//span[text()="查询"]')
    query_button.click()
    select= WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="el-link__inner" and text()="选择"]')))
    select_button = automation.driver.find_element(By.XPATH, '//span[@class="el-link__inner" and text()="选择"]')
    select_button.click()
    confirm_button=action_chains.move_to_element(automation.driver.find_element(By.XPATH,'//button[@class="el-button el-button--primary el-button--default"]/span[text()=" 确认 "]'))
    confirm_button.click().perform()
    print("客户组织选择完成")

    # 滚动到特定元素
    more_button= WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="el-link__inner" and text()="查看更多"]')))
    more_button = automation.driver.find_element(By.XPATH, '//span[@class="el-link__inner" and text()="查看更多"]')
    more_button.click()
    time.sleep(3)
    print("查看更多")

    #雇员信息
    employee_param=automation.driver.find_element(By.ID, "employee")

    id_code = WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="证件号"]')))
    id_code_input = id_code.find_element(By.XPATH, './following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
    id_code_input.send_keys("431548199908173632")
    automation.driver.switch_to.active_element.send_keys(Keys.TAB)
    time.sleep(3)

    emp_name = WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="姓名"]')))
    emp_name_input = emp_name.find_element(By.XPATH, './following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
    emp_name_input.send_keys("Auto1")
    time.sleep(1)

    emp_phone = WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="手机号"]')))
    emp_phone_input = emp_phone.find_element(By.XPATH, './following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
    emp_phone_input.send_keys("13004090110")
    time.sleep(1)


    emp_email = WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="邮箱"]')))
    emp_email_input = emp_email.find_element(By.XPATH, './following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
    emp_email_input.send_keys("13004090110@qq.com")
    time.sleep(1)

    #定位一般的 请选择
    onboarding_selects = automation.driver.find_elements(By.CLASS_NAME,"el-select")

    #选择文化程度
    education_select=onboarding_selects[8]
    education_select.click()
    time.sleep(1)
    education_select_bachelor=automation.driver.find_element(By.XPATH, "//span[text()='大学本科']")
    education_select_bachelor.click()
    time.sleep(1)

    #选择民族
    ethnic_select = onboarding_selects[9]
    ethnic_select.click()
    time.sleep(1)
    ethnic_select_hanzu=automation.driver.find_element(By.XPATH, "//span[text()='汉族']")
    ethnic_select_hanzu.click()
    time.sleep(1)

    #选择政治面貌
    party_select = onboarding_selects[10]
    party_select.click()
    time.sleep(1)
    party_select_populace=automation.driver.find_element(By.XPATH, "//span[text()='群众']")
    party_select_populace.click()
    time.sleep(1)

    #婚姻状态
    marriage_select = onboarding_selects[11]
    marriage_select.click()
    time.sleep(1)
    marriage_select_populace = automation.driver.find_element(By.XPATH, "//span[text()='未婚']")
    marriage_select_populace.click()
    time.sleep(1)



    #户籍地址邮编
    domicile_address_id = WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="户籍地址邮编"]')))
    domicile_address_id_input = domicile_address_id.find_element(By.XPATH, './following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
    domicile_address_id_input.send_keys("111222")
    time.sleep(1)

    #户籍地址-省市区(县)
    domicile_address_selects = employee_param.find_elements(By.CSS_SELECTOR, "input.el-input__inner[readonly][placeholder='请选择']")
    domicile_address_select=domicile_address_selects[0]
    domicile_address_select.click()
    time.sleep(1)
    domicile_address_select_province = automation.driver.find_element(By.XPATH, "//span[text()='河北省']")
    domicile_address_select_province.click()
    time.sleep(1)
    domicile_address_select_city = automation.driver.find_element(By.XPATH, "//span[text()='秦皇岛市']")
    domicile_address_select_city.click()
    time.sleep(1)
    domicile_address_select_district = automation.driver.find_element(By.XPATH, "//span[text()='海港区']")
    domicile_address_select_district.click()
    time.sleep(1)

    #户籍详细地址
    domicile_address_code = WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="户籍地址-详细地址"]')))
    domicile_address_code_input = domicile_address_code.find_element(By.XPATH, './following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
    domicile_address_code_input.send_keys("海港区小南门街道a")
    time.sleep(3)

    #联系/居住地址-省市区(县)
    #contact_address_selects = employee_param.find_elements(By.CSS_SELECTOR, "input.el-input__inner[readonly][placeholder='请选择']")
    contact_address_select=domicile_address_selects[1]
    contact_address_select.click()
    time.sleep(1)
    panels=automation.driver.find_elements(By.CLASS_NAME,"el-cascader-panel")

    panel=panels[0]
    contact_address_select_provinces = panel.find_elements(By.XPATH, "//span[text()='山西省']")
    contact_address_select_provinces[1].click()
    time.sleep(1)

    contact_address_select_city = panel.find_element(By.XPATH, "//span[text()='太原市']")
    contact_address_select_city.click()
    time.sleep(1)

    contact_address_select_district = panel.find_element(By.XPATH, "//span[text()='迎泽区']")
    contact_address_select_district.click()
    time.sleep(1)

    # 联系/居住地址详细地址
    contact_address_code = WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="联系/居住地址-详细地址"]')))
    contact_address_code_input = contact_address_code.find_element(By.XPATH,'./following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
    contact_address_code_input.send_keys("海港区小南门街道b")
    time.sleep(1)


    #居住地址邮编
    residential_address_id = WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="居住地邮编"]')))
    residential_address_id_input = residential_address_id.find_element(By.XPATH, './following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
    residential_address_id_input.send_keys("111666")
    time.sleep(1)

    #选择组合报价单
    quote = automation.driver.find_element(By.XPATH, '//span[@class="" and contains(., "选择组合报价单")]')
    quote.click()
    time.sleep(3)

    quote_popup = WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="组合报价单号"]')))
    # 2. 以 org (label) 为父级，向下查找 input
    quote_code = quote_popup.find_element(By.XPATH,'./following-sibling::div//input[@class="el-input__inner" and @placeholder="请输入"]')
    quote_code.send_keys("2000000347")
    query_button = automation.driver.find_element(By.XPATH, '//button//span[text()="查询"]')
    query_button.click()
    select= WebDriverWait(automation.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="el-link__inner" and text()="选择"]')))
    select_button = automation.driver.find_element(By.XPATH, '//span[@class="el-link__inner" and text()="选择"]')
    select_button.click()
    confirm_button=action_chains.move_to_element(automation.driver.find_element(By.XPATH,'//button[@class="el-button el-button--primary el-button--default"]/span[text()=" 确认 "]'))
    confirm_button.click().perform()
    time.sleep(3)
    print("选择组合报价单完成")

    #driver.switch_to.active_element.send_keys(Keys.PAGE_DOWN)
    #time.sleep(1)

    #actions = ActionChains(driver)
    #for _ in range(6):
    #    actions.send_keys(Keys.TAB).pause(0.3)
    #actions.perform()

    time.sleep(1)
    service_param=automation.driver.find_element(By.ID, "param")
    onboarding_params=service_param.find_elements(By.CLASS_NAME, "el-text")
    social_param=onboarding_params[6]
    house_param=onboarding_params[9]
    #print(house_param.get_attribute('outerHTML'))

    #输入社保类服务参数工资
    onboarding_params_inputs=service_param.find_elements(By.CLASS_NAME,"el-input__inner")
    social_salary_input=onboarding_params_inputs[3]
    social_salary_input.send_keys("60000")
    time.sleep(1)

    #选择合同签订方式
    onboarding_params_selects=service_param.find_elements(By.CLASS_NAME,"el-select__suffix")
    contract_method=onboarding_params_selects[4]
    contract_method.click()
    time.sleep(1)
    contract_method_option = WebDriverWait(service_param, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'初签')]")))
    contract_method_option.click()

    #输入公积金类服务参数工资
    house_salary_input=onboarding_params_inputs[6]
    house_salary_input.send_keys("60000")
    time.sleep(1)

    #选择单位比例
    company_percent=onboarding_params_selects[6]
    company_percent.click()
    time.sleep(1)
    company_percent_select = automation.driver.find_element(By.XPATH, "//span[text()='7.00%']")
    ActionChains(automation.driver).move_to_element(company_percent_select).click().perform()
    time.sleep(1)

    # 选择个人比例
    individual_percent = onboarding_params_selects[7]
    individual_percent.click()
    time.sleep(1)
    percents=automation.driver.find_elements(By.XPATH, "//span[text()='7.00%']")
    individual_percent_select = percents[2]
    individual_percent_select.click()
    time.sleep(1)

    #起缴年月（补充公积金）
    selections = service_param.find_elements(By.CLASS_NAME, "el-input__inner")
    supplementary_pension_selection = selections[8]
    ActionChains(automation.driver).move_to_element(supplementary_pension_selection).click().perform()
    time.sleep(1)
    cell_months = automation.driver.find_elements(By.CLASS_NAME, "cell")
    supplementary_pension_month=cell_months[47]
    print(supplementary_pension_month.get_attribute('outerHTML'))
    supplementary_pension_month.click()
    time.sleep(3)

    #单位比例（补充公积金）
    new_selections = automation.driver.find_elements(By.CLASS_NAME, "el-select")
    time.sleep(1)
    supplementary_pension_company_select=new_selections[21]
    supplementary_pension_company_select.click()
    time.sleep(1)
    supplementary_pension_company_percent_select = automation.driver.find_element(By.XPATH, "//span[text()='5.00%']")
    supplementary_pension_company_percent_select.click()
    time.sleep(1)

    # 个人比例（补充公积金）
    supplementary_pension_individual_select = new_select=new_selections[22]
    supplementary_pension_individual_select.click()
    time.sleep(1)
    supplementary_pension_percents=automation.driver.find_elements(By.XPATH, "//span[text()='5.00%']")
    supplementary_pension_individual_percent_select = supplementary_pension_percents[2]
    supplementary_pension_individual_percent_select.click()
    time.sleep(1)

    #for i, input_element in enumerate(domicile_address_selects):
    #    print(f"=== 输入框 {i + 1} ===")
    #    print(input_element.get_attribute('outerHTML'))
    #    print("\n")

    print("End")