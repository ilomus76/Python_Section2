#데이타를 수집하는 가장 안전한 방법은 각 기관/업체에서 제공하는 Open API를 사용
#대표적인 Open API : 공공데이터포털 , 카카오 API , 네이버 API... 매우 많다.

#[1] 공공데이터 포털 : data.go.kr   : 이용 안내 먼저 확인
# 오픈API 소개
# 오픈API란 누구나 사용할 수 있도록 공개된 API를 말합니다. 데이터를 표준화하고 프로그래밍해 외부 소프트웨어 개발자나 사용자들과 공유하는 프로그램입니다. 개방된 오픈API를 이용해 다양하고 재미있는 서비스나 애플리케이션, 다양한 형태의 플랫폼을 개발할 수 있습니다.
# *API란? Application Programming Interface의 약자로 응용 프로그램 프로그래밍 인터페이스를 말합니다. 다양한 응용 프로그램에 사용할 수 있는 운영 체제, 혹은 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스입니다.
# TIP! 유용하게 사용하는 법!
# 업데이트가 빈번하고 이용자가 많은 대용량 데이터를 제공해야 할 때, 공공데이터 포털을 통한 계정 발급 필요할 때 사용할 수 있어요.
# 날씨나 교통 정보 등 실시간 업데이트되는 데이터를 제공 받을 수 있고, 소프트웨어 개발자나 사용자들이 쉽게 활용할 수 있어 개발 비용 절감, 개발 기간 단축 등 다양한 장점이 있어요.

# https://www.data.go.kr/data/15043696/openapi.do
# https://www.data.go.kr/data/15043696/openapi.do



#회원가입해야 사용할 수 있다. 
# 심야 약국 검색 
# 오픈 API 
# 제주도 심야약국 -> 활용신청 

# [제주도 심야약국 정보 xml 수집]
import requests
#심야약국 리스트 open api end-pint url  : ? 뒤의 파라미터를 제외한 url 

# url = 'http://data.jeju.go.kr/rest/nightpharmacy/getNightPharmacyList?serviceKey=e6ab422b2d06612b99c5abcd24e6c86a73306c040f039854b0340d46cd3b9f93&pageSize=10&startPage=1 '
url = 'http://data.jeju.go.kr/rest/nightpharmacy/getNightPharmacyList'

#서비스키를 포함한 파라미터 dict
params={
    'serviceKey':'e6ab422b2d06612b99c5abcd24e6c86a73306c040f039854b0340d46cd3b9f93',
    'pageSize': 10,
     'startPage':1
}

#url과 params를 get 방식으로 요청
response = requests.get(url,params=params)
# print(response.text) # xml 형식의 문자열 출력

#xml 문자열을 분석하여 특정 요소들의 값들만 추출
import xml.etree.ElementTree as ET

root = ET.fromstring(response.text) # ET가 스트링을 가져온다.  
# 문자열을 XML로 해석(parse)하여 Element 객체를 생성,XML 문서의 최상위(Root) 태그를 가리키는 객체


#약국 정보들을 가진 요소들 찾기
pharmacy_datas = root.find('body').find('data').findall('list') #find 하나만 찾고 findall은 다 찾음.

#약국 정보들 주에서 원하는 데이터만 추출 
pharmacy_list=[] 
for pharmacy in pharmacy_datas:
    name = pharmacy.find('dataTitle').text  # 뷰티플소프트는 string으로 가져오고 xml은 text로 옴.
    address = pharmacy.find('adres').text
    tel = pharmacy.find('telNo').text
    latitude = pharmacy.find('la').text
    longitude = pharmacy.find('lo').text

    #약국 1개의 정보르 dict 만들어서 리스트에 추가 
    pharmacy_list.append({'name':name , 'address':address, 'tel':tel, 'geolocation':[latitude,longitude]})


#출력 
for pharmacy in pharmacy_list:
    print(pharmacy) # dict 데이터들 출력 


# 이 정보를 기반으로 지도에 표시하거나 데이터 분석에 사용.













# 바이브코딩
# 공공 데이타 망의 api에 접속해서 공공데이타 open API 를 xml로 받아서 스크랭핑하려고 합니다. 파이썬 코드를 작성해 주세요


# #chat Gpt 결과 

# # 공공데이터포털(OpenAPI)은 대부분 REST API 방식입니다. XML 형식으로 데이터를 받아온 뒤, xml.etree.ElementTree 또는 BeautifulSoup로 XML을 파싱하면 됩니다.

# # 아래는 가장 일반적인 형태의 예제입니다.

# # 1. requests 설치
# # pip install requests
# # 2. XML 데이터를 받아오는 코드
# import requests

# # 본인의 서비스키
# SERVICE_KEY = "여기에_발급받은_서비스키"

# url = "https://apis.data.go.kr/예시API주소"

# params = {
#     "serviceKey": SERVICE_KEY,
#     "pageNo": "1",
#     "numOfRows": "10",
#     "resultType": "xml"
# }

# response = requests.get(url, params=params)

# print(response.status_code)

# # XML 출력
# print(response.text)



# 3. XML 파싱
# import requests
# import xml.etree.ElementTree as ET

# SERVICE_KEY = "여기에_서비스키"

# url = "https://apis.data.go.kr/예시API주소"

# params = {
#     "serviceKey": SERVICE_KEY,
#     "pageNo": "1",
#     "numOfRows": "10"
# }

# response = requests.get(url, params=params)

# root = ET.fromstring(response.content)

# # XML 구조 확인
# print(root.tag)

# # 모든 item 출력
# for item in root.iter("item"):

#     name = item.findtext("name")
#     address = item.findtext("addr")

#     print(name, address)