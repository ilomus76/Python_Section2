#handle : 브라우저의 창(tab)마다 다른 handle 값(일종의 식별자)을 가지고 제어 가능
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach',True)
chrome = webdriver.Chrome(options=options)


chrome.get('https://www.w3schools.com/tags/att_input_type_checkbox.asp')
print(chrome.title)


#현재 핸들값 확인간으
current_handle = chrome.current_window_handle
print(current_handle)
time.sleep(2)


#[Try it yourself]요소를 클릭하여 새탭이 만들어짐. 
chrome.find_element(By.XPATH,'//*[@id="main"]/div[2]/a').click()
time.sleep(2)

#새팁이 생겼으니 핸들이 여러개..
handles = chrome.window_handles
for handle in handles:
    chrome.switch_to.window(handle)
    print(chrome.title)
    time.sleep(1)


#현재 탭 닫기
chrome.close()

chrome.switch_to.window(current_handle) # 처음에 저장했던 힌드.. 메인 페이지
print(chrome.title)

