import os

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Load te driver.
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Remote(
    command_executor=os.getenv('REMOTE_CHROME_DRIVER'),
    options=options,
)
url_list = [
    'https://www.one-line.com',
    'https://us.one-line.com',
    'https://ca.one-line.com',
]

try:
    for url in url_list:
        # Forward to the one-line.com.
        driver.get(url)
        # Wait util the dom loaded.
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-content"))
        )
        try:
            slideshow_blocks = driver.find_element(By.CLASS_NAME, 'slideShow-blocks')
        except NoSuchElementException as e:
            e.msg = url + e.msg
            raise e
        print(url + 'The slideshow is exist.')
except NoSuchElementException as e:
    print(e.msg)
    raise e
finally:
    driver.close()
