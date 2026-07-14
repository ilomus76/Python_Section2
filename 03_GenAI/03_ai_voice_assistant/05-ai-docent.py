## 기본 정보 입력 
# 스트림릿 패키지 추가
import streamlit as st

#OpenAI 패키지 추가
from openai import OpenAI

#이미지를 처리하기 위한 파이썬 기본 패키지
import os
import io
import base64
from PIL import Image

from dotenv import load_dotenv
load_dotenv()


#GPT-4V와 TTS를 위해서 client 객체를 선언 
# api_key ="OpenAI API 키"
# client = OpenAI(api_key=api_key)
client =OpenAI()

## 기능 구현 함수 정리
#GPT-4V

def describe(text):
    # pass

    # 엤날방식
    # response = client.chat.completions.create(

    #         model='gpt-4 turbo', 
    #         #ai-summarize.py
    #         messages = [
    #             {
    #                 'role':'user',
    #                 'content':[
    #                         {'type':'text','text':'이 이미지에 대해서 아주 자세히 묘사해줘'},
    #                         {'type':'img_url',
    #                         'img_url':{
    #                                     'url': 'https://www.gospeltoday.co.kr/news/photo/202303/10643_20129_5731.jpg',
    #                                     }
    #                         },
    #                         ],
    #             },
    #         ],
    #         max_tokens=1024,
    #     )
    # return response.choices[0].message.content



    instruction = '''
    ** role **
       너는 이미지를 보고 한국어로 설명을 해주는 가이드하는 사람이야.

    ** task **
    - 전달된 글을 한국어로 요약해라.
    - 핵심 개념을 중심으로 이미지를 간단하게 요약해서 설명해줘.
    - 내용을 3줄이내로 요약해라.
    - bullet 점을 이용해라. 


    '''


    response = client.responses.create(
            model='gpt-4o-mini', #'gpt-4.1-mini',
            instructions=instruction, #시스템 지침
            # input='https://www.gospeltoday.co.kr/news/photo/202303/10643_20129_5731.jpg',
            input=text,
            max_output_tokens=1024,
        )

    return response.output_text   # 메타 데이타 없이 줌



#TTS 
def TTS(reponse):
    # pass
    with client.audio.speech.with_streaming_response.create(
        model='tts-1',
        voice='onyx',
        input=reponse,

    ) as response:
        filename = "output.mp3"
        response.stream_to_file(filename)


    #저장한 음성 파일을 자동 재생
    with open(filename, 'rb') as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        #HTML 문법을 사용하여 자동으로 ㅇ음원을 재생하는 코드를 작성
        # #스트림릿에서 HTM을 사용할 수 있는 st.markdown()을 활용
        md = f'''
        <audio autoplay="True">
            <source src="data:audio/mp3;base64,{64}" type = "audio/mp3">
        </audio>
        '''
        st.markdown(md,unsafe_allow_html=True)
    os.remove(filename)





## main 함수 
def main():
    st.image('./ai.png',width=200)
    st.title("이미지를 해설해드립니다.")

    #이미지를 업로드 
    types=["png", "jpg", "jpeg"]
    # img_file_buffer = st.file_uploader('Upload a PGN image',type='png')

    img_file_buffer = st.file_uploader(
    "이미지를 업로드하세요", 
    type = types,
    # type=("png", "jpg", "jpeg")
)

    if img_file_buffer is not None:
        image=Image.open(img_file_buffer)
    
        #업로드한 이미지를 화면에 출력 
        # st.image(image, caption = 'Uploaded Image.', use_column_width=True)
        st.image(image, caption = 'Uploaded Image.', width="stretch")
        # st.image("./ai.png", width="stretch")


        #이미지 => 바이트 버퍼로 변환
        buffered = io.BytesIO()
        # image.save(buffered, format='PNG')
        image.save(buffered, format=image.format)

        #바이트 버퍼 => base64 인코딩 바이트 문자열로 변환
        img_base64 = base64.b64encode(buffered.getvalue())

        #base64 인코딩 바이트 문자열 => UTF-8 문자열로 디코딩
        img_base64_str = img_base64.decode('utf-8')

        #GPT-4V에서 입력받을 수 있는 형태로 변환
        #예시 참조 : https://platform.openai.com/docs/guides/vision/uploading-base-64-encoded-images
        image = f"data:image/jpeg; base64,{img_base64_str}"

        #GPT4V가 이미지에 대한 설명을 반환하고 이를 st.info()로 출력
        text = describe(image)
        st.info(text)

        #이미지에 대한 설명을 음성으로 변환
        TTS(text)


if __name__ == "__main__":
    main()







# from openai import OpenAI
# from pathlib import Path
# from dotenv import load_dotenv
# import streamlit as st


# load_dotenv()
# client = OpenAI()



# # def askGpt(prompt,apikey): # 사용자한테 키를 받음.
# #     client = OpenAI(api_key=apikey) # 사용자가 입력한 openai api key사용 : 이렇게 하면 사용자 키를 사용하니 개발자 돈이 나가지 않음.

# #     #AI 답변 지침을 정의하기( 이것이 프롬프트 엔지니어링이라고 함)
# #     #여러줄 쓸거기 때문에 ''''''을 사용 ,, 마크다운으로 할때 블릿을 많이 써라..
# #     instruction='''
# #     ** role **
# #     너는 한국어로 글을 요약하는 전문가야.

# #     ** task **
# #     - 전달된 글을 한국어로 요약해라.
# #     - 핵심 개념(Concepts)과 주장(Arguments)를 중심으로 텍스트를 요약해라.
# #     - 개념과 주제별로 3줄이내로 요약해라.
# #     - bullet 점을 이용해라. 


# #     '''










