#파이썬 지도 모듈 folium [시각화 도구] : mapplot 도 있고 이것도 있고.

# 설치 
#pip install folium : 현재 우리는 가상 머신 상황 


#1. 모듈 사용
import folium

#2. 지도가 표시될 곳의 중심좌표 [위도, 경도]
center=[37.5500,126.9900]
# 서울역 : 37.5500,126.9900
# 왕십리역: 37.5614, 127.0385
# 뚝섬역 : 37.54706945947954, 127.04740975332888
# 성수역 : 37.54461957910074, 127.05590699103249
# 건대입구역 : 37.54041716624373, 127.06914637466906

#3.지도 생성 (위 center 좌표 기준)
my_map = folium.Map(location=center,zoom_start=13, zoom_control=True) #zoom level : 1~25 숫자 클숙록 확대

#5. 미니맵 추가하기
from folium.plugins import MiniMap
#미니맵 생성
mini_map = MiniMap()
#미니팹을 내 지도에 추가하기
my_map.add_child(mini_map)

#6. 마커 추가하기
marker = folium.Marker(
    [37.5500,126.9900], #남산
    tooltip='서울역(마커에 마우스를 올리면 보여짐)',
    popup='<b>클릭하면 보이는 팝업창</b>', # html로 꾸밀 수 있음. .. 세로로 표시됨 (folium.Popup()을 사용하면 개선)

)

marker.add_to(my_map)

#7.여러개의 마카 표시
#뚝섬역
folium.Marker([37.54706945947954, 127.04740975332888]).add_to(my_map)

#성수역
html_content = '<div>성수역-여기에 긴 내용을 써도 세로로 나오지 않습니다.</div>'
iframe = folium.IFrame(html_content,width=250,height=50)
popup=folium.Popup(iframe,max_width=300)

folium.Marker(
    location=[37.54706945947954, 127.04740975332888],
    popup=popup
    
    ).add_to(my_map)

#건대입구역 icon 지정
icon = folium.Icon(

    color = 'purple', # 아이콘 배경색
    icon_color = 'white', #아이콘 이미지의 색
    icon = 'heart' #glyphicon glyphicon-heart   아이콘 종류를 제공하는 2군데 [glyphicon][fontsawesome]       ([bootstrap] 은 쓰다 맘. 왜인지 나중에 검색]
    # https://getbootstrap.com/docs/3.3/components/    

)

folium.Marker(
    location=[37.54041716624373, 127.06914637466906],
    tooltip='<i>건대입구역</i>',
    popup='<b>subway</b>',
    icon=icon


).add_to(my_map)


#8. tooltip 클릭했을 때 특정 웹사이트 열기
url ='https://www.naver.com'
popup_content = f'<a href="{url}" target="_blank">네이버로 이동</a>'
icon2= folium.Icon(color='green',icon_color='yellow',icon='flag') # 내부적으로 연결되어 있음. 
# icon2= folium.Icon(color='green',icon_color='yellow',icon='flag',prefix="") # prefix 에 사이트를 넣으면 그곳의 icon을 연결.

folium.Marker(
    location=[37.5614, 127.0385],
    tooltip='<b>왕십리역</b>',
    popup=popup_content,
    icon = icon2

).add_to(my_map)


#----------------------------------

#4. 지도를 브라우저에서 보여주기 
my_map.show_in_browser()  # 주소창에 보면 html로 되어 있음

#5. 발표 노트북에서는 그쪽 노트북을 연결할테니 그럴경우 문제
#5. 지도를 나중에 쉽게 볼 수  있도록 html파일로 저장할 수 있음.
my_map.save('./saved/my_map.html') #폴더에 가서 html을 클릭하여 사용도 가능