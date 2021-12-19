import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

current_folder = os.path.abspath(os.getcwd())
driver_path = current_folder + "/driver/chromedriver"
driver = webdriver.Chrome(driver_path)

driver.get("https://techwithtim.net")
search = driver.find_element_by_name("s")
# search = driver.find_elements_by_tag_name()
search.send_keys("django")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.ID, "main")))
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_elements_by_tag_name("header")
        for item in header:
            print(item.text)

finally:
    driver.quit()


time.sleep(5)

driver.quit()