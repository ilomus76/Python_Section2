#stream 방식 - invoke 대신에 .. stream 메소드로 요청하면 됨.

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model= ChatOpenAI(model='gpt-4o-mini',streaming=True)
# #스트림 방식으로 응답데이아를 조금씩 잘라서 받기
# response = model.stream('애국가 1절을 불러줘') # invoke는 데이타 덩어리

# for chunk in response: # 조각을 chunck
#     # print(chunk.content) #이렇게 하면 엔터친것 같음 
#     print(chunk.content,end='')

#출력을 스트림릿을 이용하여 챗봇의 글씨 하나씩 만들어 지도록....
import streamlit as st

prompt = st.chat_input('메세지를 입력하세요')
if prompt:
    #사용자 질문 채팅메세지 만들기
    with st.chat_message('user'):
        st.write(prompt)    # 이것은 덮어쓰기
    #응답 메세지를 작은 조각(chunk) 단위로 출력 
    with st.chat_message('assistant'):
        response = model.stream(prompt) # invoke를 stream으로 바꿈. 조각을 위해서
        #작은 응답을 모아놓기 위해.
        placeholder = st.empty() # 나중에 채워질 빈 공간 생성
        full_response = ""
        for chunk in response: # stream(prompt)를 나는 집에 간다를 한꺼번에 가져오는게 아니라 나는 따로 집에 따로 간다 따로 가져옴.
            full_response += chunk.content
            placeholder.markdown(full_response) # 기존 출력된 글씨를 지우고 새로 출력  
            #st.write로 하면 
            # 나는
            # 나는 집에
            # 나는 집에 간다 로 됨. 
