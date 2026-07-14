# 책 openai 51page를 할것인데 그대로 하면 에러남.

# 필요한 모듈 사용
import streamlit as st
from openai import OpenAI   # 파운데이션 모델

## ai 응답 요청기능 함수 -- 긴글 요약 #### 

def askGpt(prompt,apikey): # 사용자한테 키를 받음.
    client = OpenAI(api_key=apikey) # 사용자가 입력한 openai api key사용 : 이렇게 하면 사용자 키를 사용하니 개발자 돈이 나가지 않음.

    #AI 답변 지침을 정의하기( 이것이 프롬프트 엔지니어링이라고 함)
    #여러줄 쓸거기 때문에 ''''''을 사용 ,, 마크다운으로 할때 블릿을 많이 써라..
    instruction='''
    ** role **
    너는 한국어로 글을 요약하는 전문가야.

    ** task **
    - 전달된 글을 한국어로 요약해라.
    - 핵심 개념(Concepts)과 주장(Arguments)를 중심으로 텍스트를 요약해라.
    - 개념과 주제별로 3줄이내로 요약해라.
    - bullet 점을 이용해라. 


    '''


    # 야래의 표준 이전의 더 오래된 방식도 있었음. 

    # 표준 api 방식 ( 옛날방식 , 책에 나오는 방법)
    # response = client.chat.completions.create(
    #     model='gpt-4.1-mini',
    #     messages=[
    #         {'role':'system','content':instruction},
    #         {'role':'user', 'content':prompt}
    #     ]
    # )



    # 최신 responses api이용 : 책에는 예전방식 response사용
    response = client.responses.create(
        model='gpt-4.1-mini',
        instructions=instruction, #시스템 지침
        input=prompt,
    )

    return response.output_text   # 메타 데이타 없이 줌
#---------------------------------------------------------

#그냥 코드를 바로 쓰면. 이 문서를 다른 곳에서 import하면 바로 실행됨
def main():
    # pass
    st.set_page_config(page_title='AI 요약 프로그램')
    #매번 api_key를 입력받으면 짜증나니까.. st.session_state에 저장

    if "OPENAPI_API" not in st.session_state:  # 세션에 OPENAPI_API 키가 없다면
        st.session_state['OPEN_API'] = ''

    #사이드바
    with st.sidebar:
        openai_apikey = st.text_input(label='OPENAI API 키', placeholder='openai api 플랫폼에서 발급한 API키를 입력하세요',value='', type='password')
        #사용자가 입력한 키를 session_state에 저장
        if openai_apikey:
            st.session_state['OPEN_API']=openai_apikey
        st.markdown('---') #구분선
    
    #메인공간 
    st.header('📜AI 글 요약 프로그램')  # 이모지 사용하고 싶으면 윈도우 + . 을 써라
    st.markdown('---')

    #여러줄 입력할 수 있는 입력상자
    text = st.text_area('요약할 글을 입력하세요')
    #[요약]버튼을 클릭하여 AI를 이용하여 요약한 결과를 출력
    if st.button('요약'):
        with st.spinner('AI가 응답중입니다... 잠시만 기다려주세요'):
            #ai LLM 모델에게 글을 전달하고.. streamlit의 info상자에 결과 보여주기
            response = askGpt(prompt=text, apikey=openai_apikey)
            st.info(response)


#현재 파일을 직접 실행했을을 때만 main() 기능이 동작하도록...
if __name__ == '__main__':
    main()
