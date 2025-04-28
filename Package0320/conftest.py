import pytest
import time
import html
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#修改html日志标题
def pytest_html_report_title(report):
	report.title = "调派订单UI自动化报告"


#设置日志文件动态文件名，保证每次执行生成单独的日志文件
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """ Set log file name same as test name """
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = './output/log/pytestLOG' + now + '.txt'
    # 生成日志文件
    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)
