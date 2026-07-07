# 셀레니엄 Selenium RPA 


# Step0] 해당 프로젝트를 01_RPA로 해라 
# Step1] pip install selenium     
# 
# 자동화 웹브라우저가 종료되지 않도록.. 옵션 생성
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option('detach',True)  # detach 분리하다 떼어내다 



# 과제 1] https://www.w3schools.com 접속 (URL 은 구글에서 w3schools 검색)
#1. 기본 셀리이움으로 특정 웹페이지를 열기
from selenium import webdriver
chrome = webdriver.Chrome(options)  # 기본적으로 자동화 웹브라어저는 코드를 모두 실행한 후 자동 종료됨. ( 막은것 같음) 옵션으로 계속 유지되도록...
# chrome.get('https:/www.naver.com')
chrome.get(' https://www.w3schools.com')
import time
time.sleep(3)
chrome.maximize_window()


# # 과제2 ] 화면 중간 LEARN HTML 클릭
from selenium.webdriver.common.by import By
#1)XPATH로 요소 찾기 : 브라우저에서 원하는 요소의 오른쪽 클릭 "검사 -> 해당요소 선택 -> Copy -> Copy XPATH
# p1 = chrome.find_element(아이디로...,'p1')   :=> from selenium.webdriver.common.by import By 이 필요
e = chrome.find_element(By.XPATH,'//*[@id="main"]/div[2]/div/div[1]/a[1]') # / 루트경로
print(e.text)  # 셀레니움을 찾으면 ok

# 과제3]상단 메뉴 중 HOW TO 클릭
e=chrome.find_element(By.XPATH,'//*[@id="subtopnav"]/a[12]')
print(e)
e.click()


# 과제4]좌측 메뉴 중 Contact Form 메뉴 클릭
e = chrome.find_element(By.XPATH,'//*[@id="leftmenuinnerinner"]/a[120]')
print('contact from:',e)
e.click()    
# 윈도우 사이즈가 반응형으로 움직일 경우 해당 요소가 가려질터이니 XPATH가 없어질 수도 있어 window 사이즈를 maxmization 해야 함.  
# 따라서 chrome.maximize_window() 이 위에서 선행되어야 한다. 

time.sleep(5)

# 과제5] . 입력란에 아래 값 입력

text_content = [
    {
    'First_Name': 'Hong',
    'Last_Name' : 'Kil-Dong',
    'Country'   : 'USA',
    'Subject' : '자동화 수행 완료!'
    },
    {
    'First_Name': 'Kim',
    'Last_Name' : 'Ha-Dong',
    'Country'   : 'Austrailia',
    'Subject' : '자동화 수행 완료!'
    },
    {
    'First_Name': 'Park',
    'Last_Name' : 'JaeDong',
    'Country'   : 'Canada',
    'Subject' : '자동화 수행 완료!'
    }   
    
    ]


e= chrome.find_element(By.XPATH,'//*[@id="fname"]')
print(e)
e.send_keys(text_content[0]['First_Name']) # 키보드 값을 보낸다. 
time.sleep(5)
e= chrome.find_element(By.XPATH,'//*[@id="lname"]')
print(e)
e.send_keys(text_content[0]['Last_Name']) # 키보드 값을 보낸다. 




from selenium.webdriver.support.ui import Select

e= chrome.find_element(By.XPATH,'//*[@id="country"]')
select = Select(e)


    
time.sleep(5)

for option in select.options:
    print(option.text)
    # if option == 'Australia':
    if option.text == text_content[0]['Country']:
        select.select_by_visible_text(option.text)
    else:
        print('Austrailia doesn\'t exit')



# 우리는 크롤링을 하고 있는것이고 웹페이지의 렌더링은 우리가 관여할 수 있는것은 아니다. 
e= chrome.find_element(By.XPATH,'//*[@id="main"]/div[3]/textarea')
e.send_keys(text_content[0]['Subject']) # 키보드 값을 보낸다. 


# 
#6. 3초 대기 후 Submit 버튼 클릭
time.sleep(5)
e = chrome.find_element(By.XPATH,'//*[@id="main"]/div[3]/a').click()


# 7. 3초 대기 후 브라우저 종료
time.sleep(5)
#현재 탭 닫기
chrome.close()

#-------------

# 이 코드는 Selenium에서 XPath를 이용해 요소를 찾는 코드입니다.
# from selenium.webdriver.common.by import By
# e = chrome.find_element(By.XPATH, '//*[@id="main"]/div[3]/label[4]')
# 의미는 다음과 같습니다.

# chrome.find_element() : 웹페이지에서 요소 1개를 찾습니다.
# By.XPATH : XPath 방식으로 찾습니다.
# '//*[@id="main"]/div[3]/label[4]' : id="main"인 요소 아래의 세 번째 div 안에 있는 네 번째 label을 찾습니다.
# 찾은 요소를 e 변수에 저장합니다.
# 예를 들어 클릭하려면
# e.click()
# 체크박스라면 보통 다음과 같이 사용할 수 있습니다.

# e = chrome.find_element(By.XPATH, '//*[@id="main"]/div[3]/label[4]')
# e.click()
# 만약 에러가 난다면
# 에러 메시지를 알려주시면 원인을 정확히 말씀드릴 수 있습니다. 흔한 원인은 다음과 같습니다.

# NoSuchElementException
# XPath가 잘못되었거나 아직 페이지가 로딩되지 않았습니다.
# ElementClickInterceptedException
# 다른 요소가 위를 가리고 있습니다.
# ElementNotInteractableException
# 요소가 숨겨져 있거나 비활성화되어 있습니다.
# 로딩이 끝난 후 찾는 것이 더 안전합니다.
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# e = WebDriverWait(chrome, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[3]/label[4]'))
# )

# e.click()

# 이 방법은 요소가 나타나고 클릭 가능해질 때까지 최대 10초 기다리므로 자동화에서 가장 많이 사용하는 방식입니다.

# 질문: 이 코드를 실행했을 때 어떤 에러가 발생했나요? 에러 메시지를 보내주시면 함께 해결해 드리겠습니다.





   
#    First Name : 홍 
#    Last Name : 길동
#    Country : USA   -> 이것은 AI  에게 물어봐서 해라...
#    Subject : 자동화 수행 완료!
#    ※ 위 값들은 변수로 미리 저장해두세요









# selenium
# webdriver
#   객체 와 변수가 많으니 그것을 .으로 체크해봐라 .. 그중에 하나가 Chrome() 