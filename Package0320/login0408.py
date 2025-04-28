from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.chrome.options import Options


def slide_verification(driver):
    try:
        # 1. 定位滑块和轨道
        slider = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".slide-verify-slider-mask-item"))
        )
        track = driver.find_element(By.CSS_SELECTOR, ".slide-verify-slider")

        # 2. 计算滑动距离（根据实际验证码调整）
        slider_width = slider.size['width']
        slider_location = slider.location
        track_width = track.size['width']
        track_location = track.location
        slide_distance = track_width - slider_width
        minX = slider_location['x']
        maxX = track_location['x'] + track_width - slider_width
        randomPosition = random.uniform(0.6, 0.7) * (maxX - minX)

        # 3. 模拟人类滑动
        actions = ActionChains(driver)
        actions.click_and_hold(slider).perform()

        # 计算当前步长（带随机变化）
        actions.move_by_offset(randomPosition,random.uniform(10, 15)).perform()

        # 5. 释放滑块
        actions.release().perform()
        time.sleep(0.001)

        # 6. 验证是否成功（根据页面实际提示调整）
        try:
            success = driver.find_element("css selector", "li.el-menu-item.is-active")
            success.click()
            return True
        except:
            return False

    except Exception as e:
        print(f"滑块验证失败: {str(e)}")
        return False
    pass

chrome_options = Options()
chrome_options.add_argument("--auto-open-devtools-for-tabs")  # 自动打开开发者工具
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()
try:
    # 打开目标页面
    driver.get("https://sales-sit.ifsg.com.cn/sprt/login")
    username = driver.find_element(By.CSS_SELECTOR, "input.el-input__inner[type='text']")
    username.send_keys("00000000")
    password = driver.find_element(By.CSS_SELECTOR, "input.el-input__inner[type='password']")
    password.send_keys("00000000")
    login_button = driver.find_element(By.XPATH, "//button//span[text()='登录']")
    login_button.click()

    max_attempts = 50  # 设置最大尝试次数
    target_url = "https://sales-sit.ifsg.com.cn/sprt/backgroundMgt/home"

    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt} to solve the captcha...")

        # 检查是否登录成功
        if driver.current_url == target_url:
            print("Verification successful!")
            break
        else:
            # 如果不可见，处理滑块验证码
            slide_verification(driver)

        # 可选：在每次尝试后等待一段时间，避免过于频繁的操作
        time.sleep(0.1)
    else:
        # 如果循环正常结束（即没有通过 break 退出），则执行这里的代码
        print("Failed to solve the captcha after maximum attempts.")

finally:
    time.sleep(3)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://sales-sit.ifsg.com.cn/sprt/hrsassgin/employee/employeeRosterSearch")
    time.sleep(3)
    query = driver.find_element(By.XPATH, "//span[text()='查询']")
    query.click()
    time.sleep(2)
    print("入职流程")
    onboarding = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div[1]/div[2]/div[6]/div/div/section/h4/div/div[1]/button/span")
    onboarding.click()
    time.sleep(3)
    org = driver.find_element(By.XPATH, '//span[@class="" and contains(., "选择客户组织")]')
    org.click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".el-input__inner[type='text']").send_keys("C000000269")
    print("Stop")
    #driver.quit()