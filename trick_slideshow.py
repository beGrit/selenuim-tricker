from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Load te driver.
service = Service('/Users/pocky/Program/bin/geckodriver')
driver = webdriver.Firefox(service=service, keep_alive=False)

# Forward to the one-line.com
driver.get('https://www.one-line.com')

# Wait util the dom loaded.
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "page-content"))
    )
    slideshow_blocks = driver.find_element(By.CLASS_NAME, 'slideShow-blocks')
    print('The slideshow is exist.')
except NoSuchElementException as e:
    print(e.msg)
    raise e
finally:
    driver.quit()
