import folium
from folium_test_position import POSITIONS,ICON_COLOR_BY_DISTANCE


center=POSITIONS[0]['위도, 경도']
map= folium.Map(location=center,zoom_start=13, zoom_control=True)


map_number = len(POSITIONS)
print('map_number:', map_number) # 15개의 검색 

marker=[]

# url ='https://www.naver.com'
# popup_content = f'<a href="{url}" target="_blank">네이버로 이동</a>'
# icon2= folium.Icon(color='green',icon_color='yellow',icon='flag') # 내부적으로 연결되어 있음. 


for idx in range(0,map_number):
    if POSITIONS[idx]['반경'] <= 500:
        icons = folium.Icon(
            color=ICON_COLOR_BY_DISTANCE['grade0']['color'],
            icon_color=ICON_COLOR_BY_DISTANCE['grade0']['icon_color'],
            icon=ICON_COLOR_BY_DISTANCE['grade0']['icon']
        )
    elif POSITIONS[idx]['반경'] <= 5000:
        icons = folium.Icon(
            color=ICON_COLOR_BY_DISTANCE['grade1']['color'],
            icon_color=ICON_COLOR_BY_DISTANCE['grade1']['icon_color'],
            icon=ICON_COLOR_BY_DISTANCE['grade1']['icon']
        )
    elif POSITIONS[idx]['반경'] <= 15000:
        icons = folium.Icon(
            color=ICON_COLOR_BY_DISTANCE['grade2']['color'],
            icon_color=ICON_COLOR_BY_DISTANCE['grade2']['icon_color'],
            icon=ICON_COLOR_BY_DISTANCE['grade2']['icon']
        )
    elif POSITIONS[idx]['반경'] <= 20000:
        icons = folium.Icon(
            color=ICON_COLOR_BY_DISTANCE['grade3']['color'],
            icon_color=ICON_COLOR_BY_DISTANCE['grade3']['icon_color'],
            icon=ICON_COLOR_BY_DISTANCE['grade3']['icon']
        )


    else:
        icons = folium.Icon(
            color=ICON_COLOR_BY_DISTANCE['grade4']['color'],
            icon_color=ICON_COLOR_BY_DISTANCE['grade4']['icon_color'],
            icon=ICON_COLOR_BY_DISTANCE['grade4']['icon']
        )



    marker.append(folium.Marker(
        location=POSITIONS[idx]['위도, 경도'],
        tooltip=POSITIONS[idx]['장소명'],
        # popup=f"<b>{POSITIONS[idx]['주소']}+'&nbsp'+{POSITIONS[idx]['전화번호']}</b>"
        popup=f"<a href=\"{POSITIONS[idx]['상세정보페이지 url']}\" target=\"_blank\"><b>{POSITIONS[idx]['주소']}+'&nbsp'+{POSITIONS[idx]['전화번호']}</b></a>",
        icon = icons
    ).add_to(map))

print(POSITIONS[0]['반경'])


# marker = folium.Marker(
#     location=[37.5500,126.9900], #남산
#     tooltip='서울역(마커에 마우스를 올리면 보여짐)',
#     popup='<b>클릭하면 보이는 팝업창</b>', # html로 꾸밀 수 있음. .. 세로로 표시됨 (folium.Popup()을 사용하면 개선)

# )

# marker.add_to(map)
map.show_in_browser()  # 주소창에 보면 html로 되어 있음


