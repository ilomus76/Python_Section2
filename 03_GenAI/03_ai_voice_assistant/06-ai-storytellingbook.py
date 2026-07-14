### 기본 정보 입력 #####
#스트림릿 패키지 추가
import streamlit as st
#OpenAI 패키지 추가
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#GPT-4 와 DALL-E 를 호출하는 함수
# from ch09_gpt import get_llm # ch09_gpt.py로부터 임포트 
# from ch09_dalle import get_imge_by_dalle # ch09_dalle.py로부터 임포트 


# 파이썬 기본 패키지 
import uuid
import os

#패이지 설정값
st.set_page_config(page_title='NovelGPT',layout='wide',
initial_sidebar_state='expanded')


#### 기능 구현 함수 정리

# get_output() 함수는 [시작] 버튼 또는 [진행하기]버튼을 클릭하면 실행
def get_output(_pos: st.empty, oid='',genre=''):
    pass

#새로운 스토리,질문 선택지 이미지를 반환하는 함수
def get_stro_and_image(user_choice):
    pass

# 스트리 질문 선택지 이미지를 저장하는 함수 
def add_new_data(*data):
    pass

#화면에 각 part를 출력하는 함수, 각 Part를 출력할 때마다 호출
def generate_content(stroy, decisionQuestion,choices: list, image,oid):
    pass

## 메인함수
def main():
    #타이틀 설정
    st.title(f"NOVEL GPT")
    pass

if __name__ == "__main__":
    main()
