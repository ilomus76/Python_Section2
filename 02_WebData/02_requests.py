#네트워크 작업을 쉽게 구현하도록 해 주는 외부 모듈 request

#0.설치 
#pip install requests


#1. 모듈 사용
import requests
#1] 일반 텍스트 데이터 읽기
# address = 'https://mbca2026aix.dothome.co.kr/webdata/aaa.txt'  # 나중에 나의 서버로 바꾸어서 올려라.
# url = request.urlopen(address)
# data = url.read()
# print(data) #한글이 깨짐. 표기법이 달라서 그런것임.
# print('-'*30)

#위의 것을 짧게  requests : 요청 , response : 응답 
response = requests.get('https://mbca2026aix.dothome.co.kr/webdata/aaa.txt')
print(response.status_code) #200(OK) ,404(파일없음) , 403(권한없음) 
print(response.text) # 인코딩 이미 되어 있음. 
print('-'*30)


#2] GET 방식으로 서버에 데이터를 전송하고 응답받기
data = { 'title': 'GET 테스트', 'msg':'이것은 GET 방식 테스트입니다.'} # dict type
url = 'https://mbca2026aix.dothome.co.kr/webdata/bbb.php'   # 이전에는 ? 쓰고 인코딩함. 

# 서버작업은 비동기 방식이라 어떤 데이타가 먼저 나올지 모르니 위에서 사용한 변수를 재사용하지 마라.
response2 = requests.get(url,params=data)
print(response2.text)
print('-'*30)

#3] POST 방식으로 서버에 데이터를 보내고 응답받기
data2 = { 'title':'안녕하세요','msg':'반가워요. POST 실습입니다.'}
url2 = 'https://mbca2026aix.dothome.co.kr/webdata/ccc.php'

response3 = requests.post(url2,data=data2) # get 방식에서는 params 였고 여기서는 data 임.

print(response3.text)
print('-'*30)


#4] 서버의 csv 형식의 파일 데이터 읽어보기
response4 = requests.get('https://mbca2026aix.dothome.co.kr/webdata/student.csv')
print(response4.text)





#csv 데이터를 , 를 기준으로 추출하기 (csv분석 parse )
#csv는 한줄 단위로 데이터 분리
lines = response4.text.split('\n')
print(len(lines))

#첫번째 줄을 제목줄이니. 출력모양 만들어 보기 
print('-'*70)
labels = lines[0].split(',') # ,를 기준으로 값들 분리.. 제목글씨들을 가진 리스트
for label in labels:
    print(label,end='\t\t') # 두번씩 탭을 벌려라 . 
print()
print('-'*70)

#나머지 학생들의 값들을 같은 방식으로 출력
for idx in range(1,len(lines)):
    values = lines[idx].split(',')
    for v in values:
        print(v,end='\t\t') # 8칸 간격으로 
    print()
print('-'*70)
print()

#csv 말고 tsv 라는 문서형식도 존재함. 꽤 많이 사용됨 [ tab separated values]
# 이 데이터도 위 방식처럼 parse 가능함. -- data 분석 [ 판다스 입문]에 예제가 있더라...
# for idx in range(1,len(lines)):
#     values = lines[idx].split('\t')  # 이곳만 다름
#     for v in values:
#         print(v,end='\t\t') # 8칸 간격으로 
#     print()
# print('-'*70)
# print()

# 데이타의 의미를 파악하기 어려움. 그래서 등작한 xml,json형식 

#5]  2026.07.09. 
#5] 서버의 데이터가 XML 데이터인 경우 . parsing 
response5 = requests.get('https://mbca2026aix.dothome.co.kr/webdata/student.xml')
# print(response5.text)  # XML 이 출력됨.

# XML 데이터를 분석하여 원하는 정보를 추출.  -이게 웹 스크랩핑이다.

#XML 형식의 문자열을 분석해주는 표준모듈 - 별도 인스톨 안해도 됨.
import xml.etree.ElementTree as ET # element tree , 즉 dom tree로 생각하면 됨.   # 너무 긴 것을 짧게 하기 위해 as ET

#ET 다룰때 사용하는 구성물의 용어 : 요소트리(ElementTree- Domtree 대신 ElementTree로 한는것만 다르고 HTML과 같다), 요소(Element), 속성(Attribute), 텍스트(Text : 안의 글씨)
  
#xml 형식의 문자열로 부터 ElementTree 객체를 만들고 최상위 요소(students)를 참조 
#HTML의 최상위는 html , 하지만 지금 불러오는 것으 최상위는 students


root = ET.fromstring(response5.text)

#root 요소안에 있는 자식요소들 중에서 item 이라는 태그를 가진 요소를 모두 찾기(학생 정보들)
items = root.findall('item') #리스트로 반환 # 여러명을 찾을 때 ,하나를 찾으면 find 
print(len(items))

#items 리스트안에 있는 각 item의 [이름, 나이 , 전공, 주소]  - 웹 스크랩핑 , 여기서는 파싱이라고 함.
for item in items:
    name = item.find('name').text # name이라는 요소를 찾아서 텍스트
    age = item.find('age').text
    major = item.find('major').text
    address = item.find('address').text

    print(name,age,major,address)
print()
print('-'*30)
print()
# 이 작업을 데이타 파싱이라고 함 
# 참고로 xml 파싱을 표준모듈로 하는 방법을 소개했지만.. 현업에서는 BeatifulSoup 외부모듈을 사용하기도 함. BeatifulSoup는 css selector를 사용할 수 있다.

#6] xml의 단점 . 시작 . 엔드 태그를 써서 데이타가 많아 트래픽이 많아짐.  그래서 이걸 간단히 만든것이 json 임

#6] 서버의 데이터가 json 형식일 경우. parsing (요즘 표준방식.. 가장 선호.. AI 표준통신 형식으로도 활용됨)
response6 = requests.get('https://mbca2026aix.dothome.co.kr/webdata/student.json')
print(response6.text)  # json key 하나가 property[멤버값]이고 key가 하나가 아니니 properties 라고 함  
# json 객체를 가지고 있는 어레이를 json array라고 함. 

# json 문자열의 properties를 통해 값들을 추출  - xml에서는 tag 명을 이용해서 찾음 .
# json 문자열을 python의 dictionary로 변환.. 을 해 주는 표준모듈 
import json
students = json.loads(response6.text) #dict로 변환함.  #load string [ .load()는 json 파일경로로 분석할때] 
# json.loads 의 s는 string 임.  # json = "{ 'name':'sam', 'age':20}" => 문자열임. json = { 'name':'sam', 'age':20} => python dictionary 사용할대 json['name'] , 이것으로 len()이 다름.  js 자바스크립트 js = {name:'sam',age:20}  사용할때 js.name
#json.load => 파일의 경로를 읽어 드릴때 사용. 

# dict 타입이니.. 식별자(key)를 이용하여 값을 추출
data_title = students['data_title']
print(data_title)
total_count = students['total_count']
print(total_count)



items = students['data']  # 배열 , 리스트 

for item in items:
    print(item['name'],item['address'],item['major'],item['address'])

print()
print('-'*30)
print()


# 데이타 불러오는 것은 했고  데이타 보내기 자바스크립트에서 했음 파이썬으로는 한번도 해본적 없음.
#7] 서버에 데이터와 파일 전송하기
# url = 'https://mbca2026aix.dothome.co.kr/webdata/student.json/webdata/upload.php'   # API 명세서를 보면 접근해야 할 사이트 접근하는 것이 주어진다. 
url = 'https://mbca2026aix.dothome.co.kr/webdata/upload.php'
# 보낼 데이타(문자열, 파일)를 종류별로 따로 포장하여 전송 ; 자바스크립트에서는 폼요소에 넣었었다.
data ={
    'title':'파일업로드 테스트',
    'msg':'파이썬으로 데이타를 전송해봅니다'
}

files = {
    'img': open('./newyork.jpg','rb')# 파일의 2진수(binary-byte)데이타를 전송
     #파일이 많을 경우 리스트로 표현해서 사용하면 된다. 
    }

# files = [
#     ('img[]', open('./aaa.jpg','rb')),# 파일의 2진수(binary-byte)데이타를 전송)
#     ('img[]', open('./bbb.jpg','rb')),# 파일의 2진수(binary-byte)데이타를 전송)
#     ('img[]', open('./ccc.jpg','rb')),# 파일의 2진수(binary-byte)데이타를 전송)
#      #파일이 많을 경우 리스트로 표현해서 사용하면 된다. 
#     ]  # img[]로 해야 하는 이유는 php에서 여러 파일을 받을 경우 img[]배열로 전송해야 하기 때문이다. 이것은 Html 폼 요소 공부에서 배웠다. 


#requests모듈로  데이타(문자열 ,팡ㄹ)을 전송하고 응답받기
response7=requests.post(url,data = data, files=files)
print(response7.text)
print()
print('-'*30)
print()


#8] 파일 다운로드 (표준모듈 urllib.request.urlretrieve()을 더 많이 사용 )
#우리는 requests로 하고 있으니 이것으로 하자...

# 픽사베이 사이트에서 무료버전만 받아와라. 
url = 'https://cdn.pixabay.com/photo/2019/12/16/10/44/dancing-in-the-rain-4699087_1280.jpg'

response8 = requests.get(url)
print(response8.text) # 이미지데이터(bytes)를  알수없는 글씨로 보여줌.  -글씨 깨짐
print(response8.content) #글씨가 아니라 그냥 바이너리 코드로 출력  - 2진수 출력

#파일 입출력 기능을 통해 내 컴퓨터에 바이너리 데이터를 저장 [다운로드] 
file = open('./download/aaa.png','wb') # 글씨가 아닌 바이너리로 쓰기
file.write(response8.content)
file.close() 
#---------------------------------------------
#다운로드를 하다보면 같은 파일명이 이미 존재하는 경우 (1)(2)같은 접미어가 추가되는 것 
# 이런 기능이 없다면 덮어쓰기가 됨. url의 retrieve는 무조건 덮어쓰기 임.
#이런 기능은 기본적으로 없음. 그래서 개발자가 기능을 구현해야 함.

import os
# def get_unique_filename(path):  # path:str이 없으며 path:Any 로 나옴. 타입정의
def get_unique_filename(path:str):  
    #doc string : 함수의 기능이 무엇인지 설명하는 글씨 
    '''
    이곳에는 있는 그대로 사용 . doc string  , 이것을 ai 모델이 읽고 참고함. 
    path파라미터로 받은 경로와 같은 이름의 파일이 있으면 (1),(2),....붙인 새 파일 경로 반환해주는 함수
    '''
    # pass
    #1. 전달받은 path와 같은 파일이 없다면 추가작업없이 그 경로 그대로 리턴 
    if not os.path.exists(path): #존재하지 않으면
        return path
    #2. 존재한다면.. (1)(2).. 같은 접미어를 붙이기
    base, ext = os.path.splitext(path) # 파일경로를 '확장자'를 기준으로 분리해주는 기능 
    num =1 

    while True:
        new_path = f'{base}({num}){ext}' #sample(1).txt
        if not os.path.exists(new_path):
            return new_path
        
        num +=1
#-------------------------------------------------------   

# get_unique_filename()


#파일 다운로드 (용량이 큰 파일을 다운로드 하는 방법도 같이 소개)
address = 'https://mbca2026aix.dothome.co.kr/webdata/scores.xlsx'
# 용량이 크면 트래픽이 많이 걸려 문제
response9 = requests.get(address,stream=True)  
#재생하면서 플레이가 됨 . 전체 다운하면서 플레이하는 게 아니고.. stream이 그 서비스임
#stream=True : 서버에서 오는 데이터를 자가은 조각(chunk) 단위로 읽음. 실제 다운로드의 시작은 iter_content()호출 시 시작 [iter: iteration 반복]

path_dir = './download'
filename = 'scores.xlsx'
path = os.path.join(path_dir,filename) # 사이의 경계선 /를 만들어서 붙여줌.  # 경로 + 파일명
#같은 이름이 있으면.. (1)(2) 붙여주는 함수 호출
path = get_unique_filename(path)


with open(path, 'wb') as file:
    #용량이 클경우 chunk 단위로 반복하면서 파일에 데이터를 저장
    for chunk in response9.iter_content(chunk_size=1024): # 1024byte == 1KB 씩 다운로드 
        if chunk: # 청크가 있다면 .. 없을 경우도 있음
            file.write(chunk)

print('저장완료:',path)




####################################################################

# backend 는 있다는 전제로 한것이니 backend 는 확인해라. 


#aaa.txt
# Hello python web data
# 안녕하세요. 파이썬을 이용한 웹 데이터 실습.

# student.csv

# name,age,major,address
# sam,20,AI,seoul
# robin,25,Data Science,incheon
# hong,23,web development,busan




# bbb.php
# <?php
#     header('Content-type:text/plain; charset=utf-8');

#     $title= $_GET['title'];
#     $message= $_GET['msg'];

#     echo "제목: $title \n";
#     echo "메세지: $message";
# ?>


#ccc.php
# <?php
#     header('Content-type:application/json; charset=utf-8');

#     $title= $_POST['title'];
#     $message= $_POST['msg'];

#     $response= [];
#     $response['title']= $title;
#     $response['msg']= $message;

#     //echo json_encode($response)
#     echo json_encode($response, JSON_UNESCAPED_UNICODE) # 이 옵션 없으면 데이터 깨짐. 보낼때부터 이미 utf-8로 된 데이터 여서.
# ?>