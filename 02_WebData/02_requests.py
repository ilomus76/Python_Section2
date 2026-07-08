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