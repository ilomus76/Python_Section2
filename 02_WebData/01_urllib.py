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
print(encoded_data)