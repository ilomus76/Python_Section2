#표준모듈로 웹데이터를 가져오기 실습
#실습을 위해 webdata폴더의 파일들을 dothome 서버에 업로드해라... 실습때는 강사님 서버로 나중에는 나의 서버로 올려라.

# 네트워크 작업을 수행하는 표준 모듈 사용
from urllib import request #HTTP Request 작업을 수행 

#1] 15일째 수업 ,그리고 파이썬 요약 할때도 했음.

#1] 일반 텍스트 파일 읽기
address = 'https://mbca2026aix.dothome.co.kr/webdata/aaa.txt'  # 나중에 나의 서버로 바꾸어서 올려라.
url = request.urlopen(address)
data = url.read()
print(data) #한글이 깨짐. 표기법이 달라서 그런것임.
print('-'*30)

print(data.decode('UTF-8'))  # 한글이 잘 나옮.
#2] GET 방식으로 서버에 데이터를 전송하고 응답 받기
# 이미 서버에 bbb.php을 올려놓음.

# 보낼 데이타를 dict 타입으로 준비
data = { 'title': '안녕하세요', 'msg':'반가워요. 잘되어야 하는데'}

# dict 타입을 URL 의 key=value 형태로 변환 (암호화) 모듈
from urllib import parse
encoded_data = parse.urlencode(data).encode('utf-8')
# print(encoded_data)
address='https://mbca2026aix.dothome.co.kr/webdata/bbb.php?'+ str(encoded_data) # get 방식
url = request.urlopen(address)
response=url.read() # 데이타를 보내도 받음. 
print(response.decode('UTF-8'))
print()

#3] POST로 보내도 응답 받기
url='https://mbca2026aix.dothome.co.kr/webdata/ccc.php'
req = request.Request(url,data=encoded_data,method='POST')
#요청 보내고 받는 작업을 예외처리까지 해서..
import urllib.error 
try: 
    with request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(f'Status: {response.status} ')  #200 403 404
        print(f'Body: {response_body}') # 응답 데이터
except urllib.error.URLError as e:
    print(f'Error: {e}')

#4]
# 표준모듈을 사용하면...인코딩.. 예외처리.등 해야될 작업이 많아 . 코드가 불편함. 
# 실무에서는 이를 편하게 해주는 requests 외부모듈을 선호함. 
#단 , 표준모듈 urllib는 웹 파일을 다운로드할때 여전히 많이 사용됨. - requests에는 이 기능이 없음.
url = 'https://mbca2026aix.dothome.co.kr/webdata/aaa.txt'
request.urlretrieve(url,'./download/aaa.txt')
# 3]이 방법이 가장 짧아서 이 방법을 많이 쓰고 머신러닝에도 많이 사용됨.  위의 것은 AI가 주는 코딩을 볼수 있도록 공부하는 것.
