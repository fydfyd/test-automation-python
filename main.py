import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.naver.com/")
driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click() # 셀렉터 / 로케이터
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="id"]').send_keys("username")
time.sleep(5)