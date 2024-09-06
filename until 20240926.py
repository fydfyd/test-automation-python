from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. 웹 드라이버 실행
driver = webdriver.Chrome()  # 크롬 드라이버를 실행합니다. 드라이버가 설치된 경로를 지정해야 할 수 있습니다.
driver.get("https://www.naver.com")  # 네이버 홈페이지를 엽니다.

# 2. 로그인 페이지로 이동
login_button = driver.find_element(By.XPATH, '//*[@id="account"]/div/a/i')  # '로그인' 버튼을 찾습니다.
login_button.click()  # 로그인 버튼을 클릭합니다.

# 3. 아이디와 비밀번호 입력
time.sleep(2)  # 페이지가 로딩될 시간을 잠시 기다립니다.

# 아이디 입력 필드 찾기
user_id = driver.find_element(By.XPATH, '//*[@id="id"]')  # 아이디 입력 필드를 찾습니다.
user_id.clear()  # 입력 필드에 기존에 입력된 내용이 있으면 지웁니다.
user_id.send_keys('아이디')  # 여기에 네이버 아이디를 입력하세요.

# 비밀번호 입력 필드 찾기
user_pw = driver.find_element(By.XPATH, '//*[@id="pw"]')  # 비밀번호 입력 필드를 찾습니다.
user_pw.clear()
user_pw.send_keys('비밀번호')  # 여기에 네이버 비밀번호를 입력하세요.

# 4. 로그인 버튼 클릭
login_submit = driver.find_element(By.XPATH, '//*[@id="log.login"]')  # 로그인 버튼을 찾습니다.
login_submit.click()  # 로그인 버튼을 클릭합니다.

# 5. 일정 시간 대기 후 브라우저 종료
time.sleep(5)  # 로그인이 완료될 시간을 기다립니다.
driver.quit()  # 브라우저를 종료합니다.