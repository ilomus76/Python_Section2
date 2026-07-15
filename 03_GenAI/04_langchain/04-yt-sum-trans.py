#### 기본 정보 입력 ###
# 스트림릿 패키지 추가
import streamlit as st 

# OpenAI 패키지 추가
import openai

#유튜브 동영상을 다운로드하기 위한 pytubefix 패키지 추가
from pytubefix import YouTube


#유튜브 영상을 번역, 요약하기 위한 랭체인 패키지 추가
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

#기타 필요한 기본 패키지 추가
import re
import os
import shutil

#Whisper 를 사용하기 위한 client 선언

# api_key="여기에 API 키를 넣어 주세요"
# client = openai.OpenAI(
#     api_key=api_key
# )

# api_key="여기에 API 키를 넣어 주세요"
client = openai.OpenAI()


##### 기능 구현 함수 정리 ######
#주소를 입력받아 유튜브 동영상의 음성(mp3)를 추출하는 함수
def get_audio(url):
    # pass
    yt=YouTube(url)
    audio = yt.stream.filter(only_audio=True).first()
    audio_file = audio.download(output_path=".")
    base,ext = os.path.splitext(audio_file)
    new_audio_file = base + ".mp3"
    shutil.move(audio_file,new_audio_file)
    return new_audio_file


#음성 파일 주소를 전달받아 스크립트를 추출하는 함수
def get_transcribe(file_path):
    # pass

    with open(file_path) as audio_file:
        transcript = client.audio.transcriptions.create(
            model='gpt-4o-mini',
            response_format='text',
            file=audio_file,
        )

#영어 입력이 들어오면 한글로 번역 및 블릿 포인트 요ㅑㄱ을 수행
def trans(text):
    # pass
    response = client.chat.completions.create(

        model="gpt-4o-mini",
        messages=[
            {'role':'system','content':'당신은 영한 번역기이지 요약가입니다. 들어오는 모든 입력을 한국어로 번역하고 불릿 포이트를 이용해 요약해주세요 반드시 플릿 포인트로 요약해야 합니다'}
        ]
    )
#유투브 주소의 형태를 정규 표현식으로 체크하느 함수
def youbube_url_check(url):
    pass

#### main 함수 #####
def main():
    #session state 초기화
    if "summarize" not in st.session_state:
        st.session_state['summarize']=''


if __name__=="__main__":
    main()

