#selenium : 사용자가 브라우저에서 수행하는 행동을 파이썬 코드가 대신 움직이도록 해 주는 모듈 
#웹 클롤러 : 긇어 온다.. 네이버 등 여러곳을 가서 긇어 오는것.
# or RPA 자동화 서비스 개발에 많이 활용됨.

#설치 : pip install selenium 
#셀리네움으로 웹브라우저를 제어할때 버전에 따라.. 각 브라우저의 웹드라이버를 설치해야 할 수도 있음.
# 프로그램을 할때 드라이버..
#하드웨어를 제어하는 프로그램을 드라이버... 혹은 운영프로그램이랑 연동해주는 것.
# [현재 셀리니움 버전에서는 추가설치 안해도 됨 하지만 6개월 후에 설치를 해야 할수도 있으니 구글검색에서 구글 드라이버로 검색해서 설치해라]


# 자동화 웹브라우저가 종료되지 않도록.. 옵션 생성
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option('detach',True)


#1. 기본 셀리이움으로 특정 웹페이지를 열기
from selenium import webdriver
chrome = webdriver.Chrome(options)  # 기본적으로 자동화 웹브라어저는 코드를 모두 실행한 후 자동 종료됨. ( 막은것 같음) 옵션으로 계속 유지되도록...
chrome.get('https:/www.naver.com')

import time
time.sleep(3)

# 웹 크롤링 ... 웹페이지를 돌아다니면서 데이터를 긁어오는 기술
#페이지 변경 -- 웹페이지(html)에서 데이터를 추출하는 것도 살짝 다뤄보기 위해..
#우선 간단한 .html 페이지를 만들어서 실습
# 내가 만든 웹페이지의 절대경로(전체경로)가 필요해서 만들기
import os
print( os.getcwd()) #현재 작업 위치 .. 확인

#index.html의 절대경로 만들기
chrome.get(os.path.join(os.getcwd(),'./03_web/index.html'))
time.sleep(2)
#셀레니움이 이용하여 웹페이지안에서 데이터를 수집하기!!  -> 우리의 전공분야...

from selenium.webdriver.common.by import By
#1)아이디로 요소 찾기  -> 뷰티블 소프와 좀 다름
# p1 = chrome.find_element(아이디로...,'p1')   :=> from selenium.webdriver.common.by import By 이 필요
p1 = chrome.find_element(By.ID,'p1')   
print(p1.text)


#2) 클래스명으로 요소들 찾기
es = chrome.find_elements(By.CLASS_NAME,value='aaa')
print(len(es)) #1 개
print(es[0].tag_name) # div

#3. 태그이름 
es = chrome.find_elements(By.TAG_NAME,value='h2')
# print(es[0].text)
for e in es:
    print(e.text) # TITLE, 파이썬 자동화 실습


#4. CSS선택자로 찾기
es = chrome.find_elements(By.CSS_SELECTOR,'ul.sss>li>a')
for e in es:
    print(e.text) #네이버 , 구글 , 다음

#5. xPath ---요소를 쉽게 찾기 위한 경로...

e = chrome.find_element(By.XPATH,"/html/body/div/p/strong") # / 루트경로
print(e.text)  # 셀레니움을 찾으면 ok

#6. 링크 텍스트로 찾기
e = chrome.find_element(By.LINK_TEXT,"네이버")
print(e.get_attribute('href')) #속성값 취득

#7. input 요소에 글씨 입력하기
e = chrome.find_element(By.NAME, 'title')
e.send_keys('자동화 글씨 입력') # 키보드 값을 보낸다. 
print(e.get_attribute('value'))


#선택한 요소를 제어하기 (클릭하기)
time.sleep(2)
e=chrome.find_element(By.LINK_TEXT,"구글")
e.click()

time.sleep(2)
chrome.back()

time.sleep(2)
chrome.forward()

time.sleep(2)
chrome.refresh()
