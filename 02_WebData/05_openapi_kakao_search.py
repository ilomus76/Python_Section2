# 공공 데이터 외에도 많은 정보를 가진 디지털기업도 자사의 정보를 활용하여 
#사용자에게 유용한 애플리케이션을 제작할 수 있도록 OPEN API를 제공하고 있음.

#https://developers.kakao.com/
# kakao, naver의 apikey 방식이 달라 각각 실습으로 경험해 보기.
# 키발급은 ai가 해주지 않음 이것은 우리가 해야함.

#카카오의 [로컬검색 API : 특정키워드를 주면 해당 키워드에 해당하는 장소들에 대한 정보(상호,위도 , 경도 , 소개페이지 url)]를 json으로 제공해주는 api
# 카카오 사이트 로 가야 함 .
# 카카오 개발자 사이트로 가야함. 가이드 문서 확인 . 키 발급 (REST API KEY) -> 자바스크립트키와 다름  
# id : gmail 계정 


##########################################
# REST API 키    : 앱 , 웹 이외 다른것들    
# JavaScript 키 : 웹개발  
# 네이티브 앱 키  : 앱 개발 


import requests

#end point url
# url ='https://dapi.kakao.com/v2/local/search/keyword.${FORMAT}'
url ='https://dapi.kakao.com/v2/local/search/keyword.json'


#인증키는 url이 아닌. header에 넣어서 전송하라고 함. GET방식으로 해야 한다고 카카오에 나와 있음.
# REST API 키 Authorization: KakaoAK ${REST_API_KEY}
headers  = {'Authorization':'KakaoAK 4d36eab055506df003ca8f606fce81d5'}

# 요청 파라미터 들 
params = { 'query':'스타벅스','x':'126.9296','y':'37.48422', 'radius':'15000', 'sort':'distance'} # query은 필수 항목으로 설명이 카카오에 나와있다. 나머지는 옵션
# query , 경도 , 위도 , 반경, 정렬은 거리순. 

# 요청 과 응답  : 자바스크립트에서는 내려받아 그리고나서 처럼 3줄을 파이썬에서 한줄로 끝
response = requests.get(url,headers=headers,params=params)
# print(response.text) # 응답 확인

#json형식은 응답문자열에서 원하는 정보를 추출 (장소명,주소)
response_dict = response.json() # json -->dict로 바꾼것임. 
items = response_dict['documents']

print('POSITIONS=[')
for item in items:
    # print('장소명:', item['place_name'])
    # print('주소:', item['road_address_name'])
    # print('전화번호:', item['phone'])
    # print('위도, 경도:', item['y'],",",item['x'])
    # print('상세정보페이지 url:', item['place_url'])
    
    print("{'장소명':", f'"{item['place_name']}"',',')
    print("'주소':", f'"{item['road_address_name']}"',',')
    print("'전화번호':", f'"{item['phone']}"',',')
    print("'위도, 경도':", "[",item['y'],",",item['x'],"]",',')
    print("'상세정보페이지 url':", f'"{item['place_url']}"',',')
    print("'반경':", item['distance'],'},')
    print('#-'*40)
    print()
    
print(']')

    


#5교시
# 이 정보들을 지도로 보여주기 - 파이썬에서도 지도를 보여줄수 있는 모듈이 있다. folium[이쁘지 않아요.. 실무에서는 웹으로 데이터를 보내고 이를 지도로 보여줌.]
# 데이터분석용으로 특정지역 상점밀집도, 유동인구 분포등을 시각적으로 간단하게 시각화해야 할때 사용.

# 파이썬 지도 모듈 실습 [ 06번 파일에서 하자.. 06_map_folium.py]

# [수행과제] 위 정보들을 지도에 표시하기 
#1. 위 장소들의 위도, 경도 정보를 이용하여 마커 표시
#2. 마커의 툴팁에는 [상호명(장소명)]이 표시
#3. 마커의 팝업에는 [주소,전화번호]가 표시 
#4. 각 마커의 팝업을 클릭하면 장소들의 [상세정보페이지 url]을 이용하여 새탭으로 정보 보여주기

#5.장소별 카테로리 구분에 따라 마커의 색상을 다르게 표시  -거리에 따라 카테고리에 따라 색상 구분 - 카카오 맵에서 속성 보고 
#(지도 시각화 사례 조사)
#구글 이미지 검색 : '데이터분석 지도 시각화'


