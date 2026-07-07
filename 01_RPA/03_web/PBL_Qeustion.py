# Quiz) Selenium 을 이용하여 아래 업무를 자동으로 수행하는 프로그램을 작성하시오

# 1. https://www.w3schools.com 접속 (URL 은 구글에서 w3schools 검색)
# 2. 화면 중간 LEARN HTML 클릭
# 3. 상단 메뉴 중 HOW TO 클릭
# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# 5. 입력란에 아래 값 입력
#   First Name : 홍
#   Last Name : 길동
#   Country : USA
#   Subject : 자동화 수행 완료!
#   ※ 위 값들은 변수로 미리 저장해두세요
# 6. 3초 대기 후 Submit 버튼 클릭
# 7. 3초 대기 후 브라우저 종료
# (공통)모든 작업 사이 1초씩 대기
# select 요소의 선택을 위해서는 모듈 추가 필요(학습하지 않았던 내용이면 AI 도움으로 해결하시오)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

# 1. https://www.w3schools.com 접속 (URL 은 구글에서 w3schools 검색)
browser.get('https://www.w3schools.com')
time.sleep(1)

# 2. 화면 중간 LEARN HTML 클릭
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()
time.sleep(1)

# 3. 상단 메뉴 중 HOW TO 클릭
browser.find_element(By.XPATH, '//*[@id="subtopnav"]/a[12]').click()
time.sleep(1)

# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[120]').click()
time.sleep(1)

# 링크 텍스트로 비교 > Contact Form 이라는 2개 이상의 링크 텍스트가 있는 경우 실패
#browser.find_element_by_link_text('Contact Form').click() 

# 가장 좋은 방법 (텍스트 전체 일치 여부 비교)
#browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() 

# 일부 텍스트 비교하는 방법
#browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()

# 5. 입력란에 아래 값 입력
#   First Name : 홍
#   Last Name : 길동
#   Country : USA
#   Subject : 자동화 수행 완료!
#   ※ 위 값들은 변수로 미리 저장해두세요

first_name = "홍"
last_name = "길동"
country = "USA"
subject = "자동화 수행 완료!"

browser.find_element(By.XPATH, '//*[@id="fname"]').send_keys(first_name)
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="lname"]').send_keys(last_name)
time.sleep(1)

# select 요소의 선택을 위해서 모듈 추가 필요
from selenium.webdriver.support.ui import Select
Select(browser.find_element(By.XPATH, '//*[@id="country"]')).select_by_visible_text(country)
time.sleep(1)

browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

# 6. 3초 대기 후 Submit 버튼 클릭
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()

# 7. 3초 대기 후 브라우저 종료
time.sleep(3)
browser.quit()
