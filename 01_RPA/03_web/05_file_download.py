#웹페이지에 있는 미디어 파일을 내 컴퓨터로 다운로드 자동화
#2가지 경우에 따라 이미지 다운로드 방식이 다름

#case1. <a>요소의 속성 중에 download 속성이 있는 경우는 링크를 클릭하면 다운로드 
#case2. <img> 요소로 이미지를 보여주는 경우 - 이미지 동영상 상관없음 src속성값을 통해 파일을 다운로드 해야 함. 


#[case1]: <a> 요소에 download 속성이 있는 경우 [연습용 웹 페이지 : download_link.html]
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach',True)

#기본 다운로드 경로를 지정하고 싶다면...
options.add_experimental_option('prefs',{'download.default_directory':r'C:\Users\Admin\MBCA\Python2\01_RPA\03_web\image'}) # 다운로드의 기본위치 지정

chrome = webdriver.Chrome(options=options) # 파마미터값을 대입 안해도 됨. 똑같기 때문에
# 다운로드 링크가 있는 웹페이지 열기
chrome.get('http://127.0.0.1:5500/01_RPA/03_web/download_link.html') # 라이브서버 주서 Live Server URL
# chrome.get('http://127.0.0.1:5500/03_web/download_link.html') # 라이브서버 주서 Live Server URL
time.sleep(2)

#다운로드 링크 요소를 찾아서 클리! .. 하면 자동 다운로드 
anchor_element = chrome.find_element(By.XPATH,'/html/body/a[2]')
anchor_element.click() # 앵커는 클릭만 하면 동작되기 때문에 클릭 

time.sleep(4)


#-----------------------------------------------------------
# [case2] img 요소로 보여주는 이미지파일을 다운로드 하기!
chrome.get('https://m.etnews.com/') #[전자신문사이트] 열기  
# 이곳의 헤드라인에 있는 이미지를 다운받기 . 이 이미지는 이동만 되고 다운이 안되는것이다.
chrome.maximize_window()
time.sleep(2)  # 너무 빨리하면 차단 당함

#헤드라인 뉴스 이미지를 가진 요소 찾기
img_element = chrome.find_element(By.XPATH,'/html/body/main/section[1]/div/figure/a/img')

#이미지요소의 src 속성값을 가져오기
img_url = img_element.get_attribute('src')

#이미지 URL 의 파일을 다운로드 하기 ! -표준  모듈로.. urllib
from urllib import request   # requests 는 외부 모듈. 다운로드 기능은 외부모듈에는 없음.

if img_url:    
    request.urlretrieve(img_url,filename='./01_RPA/03_web/image/download_image.jpg')  # 모든 파일을 다룰 수 있음.  # 라이브 서버 경로 주소를 잘 봐야 한다. 이것때문에 에러난다 
else:
    print('이미지 URL을 찾을 수가 없습니다.')