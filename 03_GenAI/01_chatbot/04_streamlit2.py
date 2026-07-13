# streamlit 사이트 : https://streamlit.io/     : 이쁘게 web을 만들수 있는 사이트

import streamlit as st

#사이드 바 - 웹사이트에서 좌측 사이드 영역을 만들때 사용

st.sidebar.title('사이드바 제목')
st.sidebar.markdown('여기에 설정을 추가할 수 있습니다')

option = st.sidebar.radio('옵션선택',['옵션A','옵션B','옵션C'])
st.sidebar.button('사이드바 버튼')
#----------------------------------

#여러개의 컬룸을 나누어서 화면 구성
col1, col2 = st.columns(2)

col1.write('첫번째 컬룸')
col2.write('두번째 컬룸')

#너비를 다르게..
col1, col2, col3 = st.columns([2,6,2]) # 너비 비율 2:6:2

with col1: #col1안에서 쓸래
    st.header('COL1')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with col2: #col1안에서 쓸래
    st.header('COL2')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3: #col1안에서 쓸래
    st.header('COL3')
    st.image('https://static.streamlit.io/examples/owl.jpg')

#Tab(탭) 만들기
tab1,tab2,tab3 = st.tabs(['cat','dog','owl'])
with tab1: #col1안에서 쓸래
    st.header('고양이')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with tab2: #col1안에서 쓸래
    st.header('강아지')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with tab3: #col1안에서 쓸래
    st.header('올빼미')
    st.image('https://static.streamlit.io/examples/owl.jpg')

#Expander - 아코디언 UI
with st.expander('더보기'):
    st.write('이곳에 추가 정보를 표시할 수 있음.')

with st.expander('고양이 정보 보기'):
    st.write('여기는 고양이에 대한 상세정보가 있어요.')
    st.image('https://static.streamlit.io/examples/cat.jpg',width=200)