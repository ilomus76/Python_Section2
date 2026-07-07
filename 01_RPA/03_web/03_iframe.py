# 페이지안에 다른페이지가 있는 경우.. 그 안의 요소찾아 제어
# 대표적으로 iframe  => https://www.w3schools.com/TAgs/tryit.asp?filename=tryhtml5_input_type_radio

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options= Options()
options.add_experimental_option('detach', True)

chrome= webdriver.Chrome(options)
chrome.get('https://www.naver.com')



#웹 화면에 바로 보이는 radio 요소 찾아보기 시도..
#
#  //*[@id="html"]


chrome.switch_to.frame('iframeResult') # frame의 id로 이동
print('프레임 이동 성공') # 호면에는 변화 없음. 

# iframe 안에 있는 요소를 찾기
e=chrome.find_element()



