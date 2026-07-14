from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st




load_dotenv()
client = OpenAI()


# response = client.responses.create(
#     model='gpt-4o-mini',
#     temperature=0.0,
#     # top_p=0.5,
#     tool_choice='required',
#     tools=[
#         {
#             "type":"web_search"
#         }
#         ],
#     timeout=20,
#     max_output_tokens=1000,
#     input='부천시의 배드민턴 구장의 전화번호 좀 얄려주세요',
#     instructions='''
#         ** role **
#         당신은 부천 배드민턴 연합회 일원이야. 부천에 있는 배드민턴 구장을 10개만 찾아줘 

#         ** task **
#         - 배드민턴 구장의 주소와 연락처를 알려주세요
#         - 주소와 연락처를 찾은 근거도 알려주세요.
#         - 무료인지 유료인지 유료라면 가격은 얼마인지 알려주세요    

#     ''' ,

# )

# print(response)
# print('-'*30)

def text_expressoin_on_streamlit():
    st.title('ChatBot Service is not supported yet')
    st.header('Service would be comming soon')
    st.subheader('The date is not defined yet')
    st.write('ChatBot 서비스를 위한 준비중에 있습니다.')

def markdown_expression():
    st.markdown('**마크다운문법 strong**') # ** 이 strong 태그임 
    st.markdown('*마크다운문법 emphasize*') # ** 이 em 태그임 
    st.markdown('# h1요소') # #다음에 띄어쓰기 
    st.markdown('## h2요소') # #다음에 띄어쓰기 
    st.markdown('### h3요소') # #다음에 띄어쓰기 
    st.markdown('#### h4요소') # #다음에 띄어쓰기   6번까지 있음.
    st.markdown('- openai')  # - 블릿기호
    st.markdown('- google genai')
    st.markdown('---') #수평선 hr


codes = [
     {'text': 'import streamlit as st', 'language':'python'},
     {'text': 
    '''
    import requests
            
    response = requests.get('https://www.naver.com')
    print(response.text)
            
    ''' , 'language':'python'},
    {
        'text':'document.write("Hello JavaScript")','language':'javascript'
    },
]



def markdown_caption(text):
    st.caption(text) #회색으로 표시 

def markdown_code(text='',language='python'):
    #AI나 머신러닝 개발자들이 본인 코드를 소개할때 사용하기 편하도록.
    #코드를 출력하는 기능 
    st.code(text,language)
    #여러줄의 코드를 출력하려면.. 세따옴표 사용
    # st.code('''
    # import requests
            
    # response = requests.get('https://www.naver.com')
    # print(response.text)
            
    #         ''',language='python')

    # #언어를 다르게 설정해도 보여짐. 다만..색상표시가 좋지 않음.. 인식을 못해서...
    # st.code('document.write("Hello JavaScript")',language='python')
    # st.code('document.write("Hello JavaScript")',language='javascript')

def streamlit_alert_message():
    st.success('정상 처리 완료')
    st.warning('주의 필요')
    st.error('에러발생')
    st.info('정보 메세지')
    


################ main() #####################
def main():

    with st.chat_message('user'): # human 과 user가 동일했는데.. 4개중에 아무거나 써도 됨. user - assistant 가 지금은 human -ai로 대응
        st.write('안녕하세요.')




    prompt = st.text_input('prompt를 입력하세요')
    if not prompt:
        st.write('') 
    else:
        st.write(f"당신은 {prompt} 를 입력하셨어요")
    streamlit_alert_message()
    text_expressoin_on_streamlit()
    markdown_expression()
    markdown_caption('2026 plan for badminton')
    markdown_code('Hello world','python')
    markdown_code('document.write("Hello JavaScript")','javascript')
    st.divider()

    

    



if __name__ == "__main__":
    main()
