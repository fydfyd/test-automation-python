from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 웹드라이버 실행 (ChromeDriver 실행)
driver = webdriver.Chrome()

# 네이버 홈페이지 열기
driver.get('https://www.naver.com')

# 네이버 홈페이지가 로드될 때까지 잠시 대기
time.sleep(5)

# 네이버 지도 아이콘 찾기 (XPath로 아이콘 요소 찾기)
map_icon = driver.find_element(By.XPATH, '//*[@id="shortcutArea"]/ul/li[8]/a')

# 네이버 지도 아이콘 클릭
map_icon.click()

# 네이버 지도 페이지가 로드될 때까지 잠시 대기
time.sleep(3)

# 지도 검색창으로 프레임 전환 (네이버 지도는 iframe 내에 있음)
driver.switch_to.frame('gnb_my_lyr_iframe')

# 검색창 요소 찾기 (검색창 XPath로 찾기)
search_box = driver.find_element(By.XPATH, '//*[@id="input_search1725676952652"]')

# 검색창에 '광화문' 입력 후 Enter 키 입력
search_box.send_keys('광화문역')
search_box.send_keys(Keys.ENTER)

# 결과 로드 대기 (검색 결과 로드가 완료될 때까지)
time.sleep(3)

# 웹드라이버 종료
driver.quit()
