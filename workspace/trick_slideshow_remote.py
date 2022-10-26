from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(
    command_executor='http://192.168.6.150:4444/wd/hub',
    options=options
)
driver.get("https://www.baidu.com/")
