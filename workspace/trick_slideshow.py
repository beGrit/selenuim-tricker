import os

import yaml
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = None
try:
    # Load te driver.
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    driver = webdriver.Remote(
        command_executor=os.getenv('REMOTE_CHROME_DRIVER'),
        options=options,
    )
    # Load the targe sites configuration.
    path = os.getenv('TARGE_SITES_FILE_PATH')
    if path is None:
        path = '/Users/pocky/Project/selenium-tricker/config/target_sites.yml'
    url_list = []
    with open(path) as sites_file:
        yaml_content = yaml.safe_load(sites_file)
        if yaml_content is not None and 'sites' in yaml_content:
            url_list = yaml_content['sites']
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
            print(url + ': The slideshow is exist.')
    except NoSuchElementException as e:
        print(e.msg)
        raise e
except ConnectionRefusedError as e:
    print(e.msg)
    raise e
finally:
    if driver is not None:
        driver.quit()
