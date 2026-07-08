
# import requests  
# pip install requests  : is required

# target_url = 'https://ilomus76.dothome.co.kr/webdata/aaa.txt'
# response = requests.get(target_url)  # GET 방식 요청 
# print(response)
# print("상태코드 :", response.status_code, end='\n')
# print("응답메시지 :", response.reason,end='\n')
# print("URL :", response.url,end='\n')
# print("헤더 :", response.headers, end='\n')
# print("본문 :",response.text, end='\n')

# data={'title':'제목','msg':'메세지'}
# target_url = 'https://ilomus76.dothome.co.kr/webdata/bbb.php'
# response2 = requests.get(target_url, params=data)
# print(response2.text)
# print('-'*30)

# <?php
#     header('Content-type:text/plain; charset=utf-8');

#     $title= $_GET['title'];
#     $message= $_GET['msg'];

#     echo "제목: $title \n";
#     echo "메세지: $message";
# ?>


# data2 = {'title':'제목', 'msg':'message'}
# target_url = 'https://ilomus76.dothome.co.kr/webdata/ccc.php'
# response3 = requests.post(target_url, data=data2 )
# print(response3.text)
# print('-'*30)
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

# target_url = 'https://ilomus76.dothome.co.kr/webdata/student.csv'
# response4 = requests.get(target_url)
# print(response4.text) 
# print(type(response4.text)) #str type
# print('-'*30)

# lines = response4.text.split('\r\n')
# print( 'lines : ', lines)
# print( 'type(lines) : ',type(lines))

# print('-'*10)
# print('\n')


# topics = lines[0].split(',')
# print(topics)

# print('='*70)
# for idx in topics:
#     print(idx, end ='\t\t')
# print()
# print('='*70)
# # print()



# for idx in range( 1,len(lines)):
#     # print(idx)
#     data_list = lines[idx].split(',')
#     # print(data_list)
#     for data in data_list:
#         print(data,end='\t\t')
#     print()
# print()
    # for data in data_list:
    #     print('data',end='\t\t')


#############################################################################
# from urllib import request
# target_url = 'https://ilomus76.dothome.co.kr/webdata/aaa.txt'
# url = request.urlopen(target_url)
# data = url.read()
# print(data) #한글이 깨짐. 표기법이 달라서 그런것임.
# print('-'*30)
# print(data.decode('utf-8'))

# data = { 'title': '안녕하세요', 'msg':'반가워요. 잘되어야 하는데'}
# from urllib import parse,request
# encoded_data = parse.urlencode(data).encode('utf-8')
# # print(encoded_data)
# address='https://ilomus76.dothome.co.kr/webdata/bbb.php?'+ encoded_data # get 방식
# url = request.urlopen(address)

# response=url.read() # 데이타를 보내도 받음. 
# print(response.decode('UTF-8'))
# print()


#3] POST로 보내도 응답 받기
from urllib import request, parse
data = { 'title': '안녕하세요', 'msg':'반가워요. 잘되어야 하는데'}
encoded_data = parse.urlencode(data).encode('utf-8')

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

