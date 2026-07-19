#OpenAI 챗봇 만들기

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI() # 하나의 봇의 객체를 만듦. ()에 key 가 없으면 환경변수에서 키를 찾음. 
response = client.responses.create(
    model='gpt-4o-mini'
    input='날씨의 실시간 무료 API를 제공해 주는 사이트를 알려주세요'
)





# https://streamlit.io/playground 에서 streamlit 관련 코드를 받을 수 있음. --시각화 





import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk



# import streamlit as st

st.title("Hello Streamlit-er 👋") # 이모지 : windown key + . 


#Streamlit Markdown의 색상 문법 :rainvow[so much] : so much를 무지개 문법으로 표현해라
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()





st.write("Streamlit has lots of fans in the geo community. 🌍 It supports maps from PyDeck, Folium, Kepler.gl, and others.")



#############################################################################################################################

## ------ pandas data 구조 ----------------
#pd.DataFrame(
#     data=[[1, 2], [3, 4]],    # 행의 데이타
#     index=['A', 'B']          # 행의 제목
#     columns=['국어', '영어']    # 열의 제목
# )

################################################################################
## ----------------------------------------------------------------------------- 
# 서울 북위 37.5666°, 경도는 동경 126.9784°
chart_data = pd.DataFrame( 
   np.random.randn(1000, 2) / [50, 50] + [37.5666, 126.9784],  # 샌프란시스코 좌표 주변의 점 1000개를 랜덤하게 생성하는 것
   columns=['lat', 'lon']) 


## ----------------------------------------------------------------------------- 
# 샌프란시스코 
# chart_data = pd.DataFrame( 
#    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],      # 표준편차 개념, numpy broadcasting 
#    # 샌프란시스코 좌표 주변의 점 1000개를 랜덤하게 생성하는 것   
#    # 평균이 0이고 표준편차가 1인 난수를 생성합니다. 크기는 (1000, 2)입니다.
#    # NumPy의 브로드캐스팅(Broadcasting) 
#    columns=['lat', 'lon']) 

# np.random.randn(3, 2) -> 결과는 아래.
# array([
#     [-1.20,  0.55],
#     [ 0.87, -1.51],
#     [ 0.32,  1.04]
# ])


################################################################################


####################### pandas의 dataframe을 streamlit의 dataframe에 연결. #######
st.dataframe(chart_data)



#######################  padas의 dataframe을 stremlit의 지도에 연결 ###############
st.map(chart_data) #그러면 샌프란시스코 주변에 점 1000개가 지도에 표시됩니다.





#########   pydeck ########################################################3
# pydeck은 지도(Map) 시각화를 위한 Python 라이브러리입니다. Streamlit에서 지도를 더 자유롭고 아름답게 표현할 수 있도록 지원합니다.

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.5666,         #37.76,      #서울 위도37.5666°, 경도는 동경 126.9784°
        longitude=126.9784,       #-122.4,
        zoom=11,
        pitch=180,                 # 0 : 위에서 바로 내려다 보는 뷰, 50 : 비스듬히 내려다 보는 정도 
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            # get_color='[200, 30, 0, 160]',   #RGBA : RGB + 투명도? 
            get_color='[255, 255, 255, 160]',   #RGBA : RGB + 투명도? 
            get_radius=200,
        ),
    ],
))