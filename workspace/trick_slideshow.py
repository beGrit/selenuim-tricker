from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import os

# Load te driver.
service = Service(os.getenv('GECHODRIVER_HOME'))
driver = webdriver.Firefox(service=service, keep_alive=False)

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
    driver.quit()
