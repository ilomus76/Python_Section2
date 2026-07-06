#모듈 : 패키지 라이브러리 , 특정 기능을 모아놓은 폴더/파일 라이브러리

# 1. 표준모듈 : 파이썬에 기본으로 내장되어 있는 모듈 . 별도의 다운로드 설치 필요 없음.[표준함수와 다르게 기능을 사용하려면 import 필요]
# 2. 외부모듈 : 별도의 다운로드 설치 필요( pin install xxxx)

#표준함수와 표준모듈과는 다른 말 . 표준함수는 import없이 사용. 표준모듈은 import가 필요

# 표준함수중 많이 사용되는 모듈 몇가지.

#1) math 모듈 : 수학적 연산 기능 모듈  - 넘파이, 판다스가 더 많이 사용
import math
print(math.cos(1)) # cosine 함수
print(math.floor(3.7)) # 소수점 내리기[바닥]
print(math.ceil(3.2)) # 소수점 올림 
# 반올림은 표준함수 round()사용 -> import 안해도 됨. 


# 모듈명을 매번 풀네임으로 쓰기 짜증
import math as m  
print(m.pow(4,2)) #4의 2제곱 16

#모듈 안에서 자주 사용하는 함수를 더 간단히 사용하기 위해..
from math import floor,cos,pow  # 리액트랑 반대  , 특정함수 가져오기
print(floor(3.8))   # math.floor를 안해도 됨 


#2. randowm 모듈 : 랜덤값을 만들어 주는 기능 모듈 
import random 

print(random.random()) # 함수 이름과 모듈이름이 같음. #0.0~ 0.99999999... 범위 
print(random.randrange(10)) #0~9

print(random.randrange(5,16)) #5~15까지 
#리스트의 값 중에 1개를 랜덤하게 뽑기 
aaa=[10,20,30,40,50]
print(random.choice(aaa)) #1개 선택
print(random.sample(aaa,3)) #3개 선택 


#로또 번호 추천
lotto = list(range(1,45)) #range로 만든 1~45를 리스트로 ..... 
print(lotto)

#번호 6개 추출

for n in range(5):
    nums = random.sample(lotto,6)
    nums.sort()
    print('당첨예상번호 : ', nums)


#3 . os 모듈 : 운영체제와 관련된 기능 모듈 (파일경로에 많이 사용)
import os 
print('현재 운영체제:',os.name) # 윈도우즈가 nt

print('현재 작업폴더:', os.getcwd) # current working directory   ML에 많이 사용
print('현재 폴더목록:',os.listdir()) #리스트 보는것 ..    ML에 많이 사용

#폴더 만들기
# os.mkdir('image') #폴더가 있으면 에러!!!
if not os.path.isdir('image'):      # image 폴더가 없으면 만들어
    os.mkdir
#폴더 삭제
if os.path.isdir('image'):
    os.rmdir('image')

#4. datetime 모듈: 날짜와 시간 모듈 
import datetime 
#현재 날짜와 시간 얻어오기
now = datetime.datetime.now() # 모듈.객체.함수 
print(now)
print(now.year, now.month, now.day, now.hour , now.minute, now.second)

#특정 날짜로 변경하기
future = now.replace(year =(now.year + 1))
print(future)
print()

#5. urllib 모듈 : 네트워크 작업 관련 모듈 
# import urllib
# import urllib 안에 많은 라이브러리가 많으니
from urllib import request #urllib모듈의 하위모듈 request 를 import 
url = request.urlopen('https://mbca2026aix.dothome.co.kr') # request야 url좀 열어줘  # 서버것을 받아올때 request 사용
data = url.read()
print(data)
print('-'*30)
print(data.decode('UTF-8'))
print('+'*50)

######################################################################
#외부모듈 사용 : pip install 로 설치... 각자마다 pip list하면 다를 것이다. venv 가상머신 환경이라서... 
#pin install requests  : 연관된 것까지 설치. pip list 하면 보인다. 

#1) requests - 네트워크작업을 urllib보다 편하게 .. 해 주는 모듈 .... 
# 크롤링 스크랩핑할때 사용할 예정.

import requests 
response = requests.get('https://mbca2026aix.dothome.co.kr') # get 방식  requests.post() post방식
print(response.text)  # decoding 안해도 한글 잘 됨. utf-8로 자동 디코딩 

#2) Beatiful Soup 모듈 : HTML문서를 분석(parsing 파싱)해주는 모듈 -- 웹 스크랩핑할때 필수
#pip install beatifulsoup4

from bs4 import BeautifulSoup #클래스임 
soup = BeautifulSoup(response.text,"html.parser") # 객체생성 #파싱할 html글씨 ,파서지정

#id가 "aa"인 요소를 선택하여 src속성값을 추출 : 스크랩핑이다 .
img = soup.select_one("#aa") #css 선택자 .. id
print( img['src'])
print()

#p요소들 모두 선택하여 글씨 추출
for p in soup.select('p'):
    print(p.string) # p요소의 string


