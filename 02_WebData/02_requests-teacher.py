#네트워크 작업을 쉽게 구현하도록 해주는 외부 모듈 request

#0.설치
#pip install requests

#1.모듈 사용
import requests

#1] 일반 텍스트 데이터 읽기
response= requests.get('https://mbca2026aix.dothome.co.kr/webdata/aaa.txt')
print(response.status_code) #200(OK), 404(파일없음), 403(권한없음)
print(response.text) #인코딩 이미 되어 있음.
print('-'*30)

#2] GET방식으로 서버에 데이터를 전송하고 응답받기
data= {'title':'GET 테스트', 'msg':'이것은 GET방식 테스트입니다.'} #dict type
url= 'https://mbca2026aix.dothome.co.kr/webdata/bbb.php'

response2= requests.get(url, params=data)
print(response2.text)
print('-'*30)

#3] POST방식으로 서버에 데이터를 보내고 응답받기
data2= {'title':'안녕하세요', 'msg':'반가워요. POST 실습입니다.'}
url2= 'https://mbca2026aix.dothome.co.kr/webdata/ccc.php'
response3= requests.post(url2, data= data2)
print(response3.text)
print('-'*30)

#4] 서버의 csv 형식의 파일데이터 읽어보기
response4= requests.get('https://mbca2026aix.dothome.co.kr/webdata/student.csv')
#print(response4.text)

#csv 데이터를 ,를 기준으로 추출하기 (csv 분석 parse)
#csv는 한 줄 단위로 데이터 분리
lines= response4.text.split('\n') #줄바꿈 문자 기준으로 분리하여 리스트로 받기
#print(len(lines))

#첫번째 줄은 제목줄이니. 출력모양 만들어 보기
print('-'*70)
labels= lines[0].split(',') # ,를 기준으로 값들 분리..제목글씨들을 가진 리스트
for label in labels:
    print(label, end='\t\t')
print()
print('-'*70)

#나머지 학생들의 값들을 같은 방식으로 출력
for idx in range(1, len(lines)):
    values= lines[idx].split(',')
    for v in values:
        print(v, end='\t\t')
    print()

print('-'*70)
print()

#csv 말고 tsv 라는 문서형식도 존재함. 꽤 많이 사용됨 [tab seprated values ]
#이 데이터도 위 방식처럼 parse 가능함.
#데이터의 의미를 파악하기 어려움. 그래서 등장한 xml, json 형식

#5] 서버의 데이터가 XML 데이터인 경우. parsing
response5= requests.get('https://mbca2026aix.dothome.co.kr/webdata/student.xml')
#print(response5.text)

#xml 데이터를 분석하여 원하는 정보를 추출

#xml 형식의 문자열을 분석해주는 표준모듈
import xml.etree.ElementTree as ET

#ET 다룰때 사용하는 구성물 용어 : 요소트리(ElementTree), 요소(Element), 속성(Attrubute), 텍스트(Text)

# xml형식의 문자열로 부터 ElementTree 객체를 만들고 최상위 요소(students)를 참조
root= ET.fromstring(response5.text)

# root요소안에 있는 자식요소들 중에서 item 이라는 태그를 가진 요소를 모두 찾기(학생 정보들)
items= root.findall('item') #리스트로 반환
print(len(items)) #3

# items 리스트안에 있는 각 item의 [이름,나이,전공,주소] 요소를 찾아 값(텍스트) 추출.
for item in items:
    name= item.find('name').text #태그명으로 찾기
    age= item.find('age').text
    major= item.find('major').text
    address= item.find('address').text

    print(name, age, major, address)
print()
print('-'*30)
print()
# xml 파싱을 표준모듈로 하는 방법을 소개했지만. 현업에서는 BeautifulSoup 외부모듈을 사용하기도 함.

#6] 서버의 데이터가 json 형식일 경우. parsing (요즘 표준방식..가장 선호.. AI 표준 통신 형식으로도 활용됨)
response6= requests.get('https://mbca2026aix.dothome.co.kr/webdata/student.json')
#print(response6.text)

#json 문자열의 properties를 통해 값들을 추출
#json 문자열을 python의 dict 로 변환.. 을 해주는 표준모듈
import json
students= json.loads(response6.text) #load string [.load()는 json파일경로로 분석할때]

#dict 타입이니.. 식별자(key)를 이용하여 값을 추출
data_title= students['data_title']
print(data_title)

total_count= students['total_count']
print(total_count)

items= students['data']
for item in items:
    print(item['name'], item['age'], item['major'], item['address'])

print()
print('-'*30)
print()

#7] 서버에 데이터와 파일 전송하기
url= 'https://mbca2026aix.dothome.co.kr/webdata/upload.php'

#보낼 데이터(문자열, 파일)를 종류별로 따로 포장하여 전송
data = {
    'title':'파일 업로드 테스트',
    'msg':'파이썬으로 데이터를 전송해봅니다.'
}

files = {
    'img': open('./newyork.jpg', 'rb') #파일의 2진수(binary- byte)데이터를 전송
}

# files = [
#     ('img[]', open('./aaa.png', 'rb')),
#     ('img[]', open('./bbb.png', 'rb')),
#     ('img[]', open('./ccc.png', 'rb')),
# ]

#request모듈로 데이터(문자열,파일)을 전송하고 응답받기
response7= requests.post(url, data=data, files=files)
print(response7.text)
print()
print('-'*30)
print()

