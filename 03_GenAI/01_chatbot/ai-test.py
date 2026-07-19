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
    

def streamlit_each_feature():
    prompt = st.text_input('prompt를 입력하세요')
    if not prompt:
        st.write('') 
    else:
        st.write(f"당신은 {prompt} 를 입력하셨어요")
    
        #6. 사용자 입력 받기
    #1) 글씨 입력 
    name = st.text_input('이름을 입력하세요.') #enter를 치면 입력돼ㅣㅁ
    st.write(f"입력된 이름 :{name}")  # 파이썬의 f-string 
    st.divider()

    #2) 숫자 입력
    # age = st.number_input('나이를 입력하세요.')
    age = st.number_input('나이를 입력하세요.',min_value=0,max_value=100,step=1)
    st.write(f"입력된 나이: {age}")
    st.divider()


    #3)슬라이더 입력
    number = st.slider('this is slider',min_value=0,max_value=100,step=2,value=24)
    st.write(f"변경된 숫자: {number}")

    #범위로 슬라이더 사용
    number_range=st.slider('this is slider',min_value=0,max_value=100,step=2,value=(24,60)) # 범위는 튜플로 값을 넣으면 됨.
    st.write(f"변경된 범위:{number_range}")
    st.write(f"최소:{number_range[0]}")
    st.write(f"최대:{number_range[1]}")
    st.divider()

    #4) 날짜 입력     내부적으로 리액트로 짠 것이다 
    selected_date = st.date_input('날짜 선택')
    st.write(f"선택한 날짜:{selected_date}")
    st.divider()

    #5) 시간 입력     내부적으로 리액트로 짠 것이다 
    selected_time = st.time_input('시간 선택')
    st.write(f"선택한 시간:{selected_time}")
    st.divider()

    #6)여러줄 입력
    #textarea같은 것
    message = st.text_area('메세지를 입력하세요.') # enter 가 줄바꿈. ctrl+enter가 입력완료  ( 챗봇은 control +enter가 줄바꿈)
    st.write(f"입력된 메세지:  \n{message}") # 띄어쓰기 2칸+\n이 줄바꿈
    st.divider()
    

        
    #7) 파일 업로드 [ 드래그 or 탐색기 선택]
    file = st.file_uploader("파일을 업로드 하세요.")
    if file is not None:
        st.write('업로드 된 파일:',file.name)
    st.divider()

    #여러개 파일 선택
    file_list = st.file_uploader("파일을 업로드 하세요.",accept_multiple_files=True)

    if file_list is not None:
        st.write("업로드된 파일 개수:",len(file_list))
        #각 파일명을 출력하고 싶다면.. file_list의 요소(file)들의 .name을 출력
        # st.info([10,20,30])
        st.info([f.name for f in file_list]) # 리스트의 컴프리헨션... 리스트 내포. 반복문을 가져와서 그것의 이름으로 나열하라... 
    st.divider()


    #8)색상 선택
    color = st.color_picker('색상을 선택하세요.',value="#00FF00")
    st.write(f"선택한 색상:{color}")
    st.divider()
    #---------------------------------

    #7. 버튼 및 선택형 입력
    #1) 기본 버튼 --클릭 이벤트 콜백함수 처리 대신 if문으로 처리
    if st.button('클릭하세요'): #버튼을 누르면 True 
        st.write('버튼이 클릭되었습니다')
    st.divider()

    #2)체크 박스
    agree = st.checkbox('동의합니까?')
    if agree:
        st.write('동의하셨습니다')
    st.divider()

    #체크박스의 라벨이 같으면 구별이 안된다면 에러발생 . [혹시 같은 라벨로 써야 한다면]
    agree2 = st.checkbox('동의합니까?',key='agree2')
    if agree2:
        st.write('동의하셨습니다')
    st.divider()


    #3)라디오 버튼
    selected_option = st.radio("옵션을 선택하세요.",options=('옵션1','옵션2','옵션3'))
    st.write(f"선택된 옵션:{selected_option}")
    st.divider()

    #4)드롭다운 선택
    fruits = st.selectbox('과일 선택하세요',options=['사과','바나나','오렌지'])
    st.write(f"선택된 과일:{fruits}")
    st.divider()

    #5) 다중 선택
    planets = st.multiselect('행성들 선택',options=['수성','금성','지구','화성','목성','토성'])
    st.write(f"선택된 행성들:{planets}")
    st.divider()

    #6) 슬라이더 중 특정 값 선택 슬라이더
    rating = st.select_slider('평가를 선택하세요',options=["매우 아니다","아니다","보통","그렇다","매우 그렇다"])
    st.write(f"선택된 평가:{rating}")
    st.divider()

    #-----------------------------------------
    #8. 미디어파일 표시
    #1)이미지 -- 이미지 라이브러리 필요 -- pillow 모듈(pip install pillow)

    from PIL import Image
    image = Image.open("./media_files/paris.jpg")
    st.image(image,caption="파리 이미지",width=100) # 단위 픽셀

    st.audio("./media_files/old_pop.mp3")
    st.video("./media_files/trailer.mp4")
    st.divider()
    #---------------------------------------------------------------
    #9. 

def streamlit_sidebar_feature():
        
    #사이드 바 - 웹사이트에서 좌측 사이드 영역을 만들때 사용

    st.sidebar.title('사이드바 제목')
    st.sidebar.markdown('여기에 설정을 추가할 수 있습니다')

    option = st.sidebar.radio('옵션선택',['옵션A','옵션B','옵션C'])
    st.sidebar.button('사이드바 버튼')
    #----------------------------------
def streamlit_feature2():
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


def my_chatbot_test1():
    with st.chat_message('user'): # human 과 user가 동일했는데.. 4개중에 아무거나 써도 됨. user - assistant 가 지금은 human -ai로 대응
        # with 안에서 작성하는 모든 출력은 그 채팅 말풍선 안에 포함됩니다
        st.write('안녕하세요.')
    
    with st.chat_message('assistant'):
        st.write('반가워요~')

    #'role'역할에 없는 명칭을 사용하면 첫글자 표시
    with st.chat_message('bot'):
        st.write('this is bot')

    with st.chat_message('sam'):
        st.write('this is sam')

    with st.chat_message('홍길동'):
        st.write('나는 홍길동입니다.')
        st.write('반가워요')
        st.button('눌러주세요')

    #한줄로 간결하게..
    st.chat_message('ai').write('한줄로써도 됩니다.')  # ai와 assistant는 같은것임.
    st.divider()

    #3) 채팅처럼 대화하는 형태가 되려면 각각의 메세지들을 리스트로 잘 보관되어 있어야 함.
    # 단, 메세지 데이터는 딕션너리로 만들어서 순서는 {역할:'', 내용:''} 구조(스키마)구조로 만들어야 함.
    messages= [
        {'role':'assistant','content':'무엇을 도와드릴까요?'},
        {'role':'user','content':'대한민국의 수도는?'},
        {'role':'assistant','content':'대한민국의 수도는 **서울**입니다.'}, # 마크다운으로 strong tag ** xx **
        {'role':'user','content':'오. 고마워~~'},

    ] # 이런것을 보통 데이타베이스에 저장해서 가져올수 있음.

    for msg in messages:

        with st.chat_message(msg['role']):
            st.markdown([msg['content']])
    st.divider()

    #3) 사용자 채팅메세지 입력 UI

    # streamlit은 react로 그리기 때문에 화면을 다시 그림. 그래서 그전께 다 지워짐. 
    # 이전 채팅메세지가 사라질것임. streamlit의 렌더링 방식때문에 .. 새로운 메세지가 입력될때마다 이 프로그램을 처음부터 다시 실행함.
    # 즉 state화면갱신과 같음. 

    # 그래서 화면이 갱신되어도 데이터를 저장하는 변수를 streamlit에서 제공함. 
    #st.session_state 라고 부름 session은 연결. 프로그램이 진행중인... 이라는 뜻. 연결되어 있을때만 상태값을 저장한다는 뜻의 session임.

    # a. message라는 이름의 변수가 st.session_state에 존재하는지 부터 확인하고 첫 문장 저장
    if "messages" not in st.session_state:
        #"messages" 라는 키워드가 없으면 session_state에 messages라는 키워드를 넣어라... 
        # a = { 'name':'test'} 
        # a.message = 'sss' 로 하면 a 가 a = {'name':'test' , 'message':'sss'} 가 됨
        # a.message = 'sss' 와 a['message'] = 'sss'는 같은 뜻임. 
        st.session_state.messages=[
            {'role':'assistant','content':'무엇이든 물어보세요'},
        ]
    #b. st.session_state 에 저장된 "message"리스트들을 채팅메세지로 그려내기
    for msg in st.session_state.messages:
        st.chat_message(msg['role']).markdown(msg['content'])

    question = st.chat_input('질문을 입력하세요') # 화면의 맨 아래쪽에 위치 - enter 입력완료. shitf-enter 줄바꿈
    if question: # 질문이 들어왔다면
        question = question.replace('\n','  \n') # 띄어쓰기 2번 \n이 줄바꿈하는 markdown
        st.session_state.messages.append({'role':'user', 'content':question})
        st.chat_message('user').write(question)

        #입력 메세지에 대해 ai 모델을 이용하여 응답하도록.. 지금은 실습을 위해....Mock데이타 목업데이타
        response = f'{question}에 대해 알고 싶군요.  \n 어쩌고 저쩌고....' # 마크 다운에서 줄바꿈은 \n앞에 띄어쓰기 2개 # 나중에 여길 ai로 해야 함.
        st.session_state.messages.append({'role':'assistant', 'content':response})
        # st.chat_message('assistant').write()
        st.chat_message('assistant').markdown(response)



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
        max_output_tokens=5000,
    )

    return response.output_text   # 메타 데이타 없이 줌
#---------------------------------------------------------

def streamlit_GPT_interaction():
    st.set_page_config(page_title='AI 요약 프로그램')
    if "OPENAPI_API" not in st.session_state:  # 세션에 OPENAPI_API 키가 없다면
        st.session_state['OPEN_API'] = ''
    


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



def ai_tts():
    #TTS : 텍스트를 자연스러운 음서응로 변환 TEXT to SPEECH

    #구글 검색 해봐라 : openai tts api  
    #https://developers.openai.com/api/docs/guides/text-to-speech

    # openai에서 제공하는 tts 모델의 price
    #1. gpt-4o-mini-tts [ 텍스트 입력 : 100만토큰 당 $0.60달러, 오디오출력 : 100만 토큰당 $1.2]
    #2. tts-1 : 백만토큰당 $15.0
    #3. tts-1-hd : 백만토큰당 $30.0 

    #1. .env 에 있는 api key값 읽어오기
    from dotenv import load_dotenv
    load_dotenv()

    from openai import OpenAI
    client = OpenAI() # 키는 않읽어와도 됨 위에서 load_dotenv()가 읽어오기 때문

    #음성으로 변환한 음성파일을 저장할 경로와 파일명 미리 지정
    from pathlib import Path
    audio_file_path= Path(__file__).parent / 'myspeech.mp3' # __file__ 현재파일이름의 경로가 출력 , 현재 실행 중인 파일이 위치한 폴더에 "speech.mp3"파일명으로 경로 만들기 
    #pathlib 를 쓰면 모듈에서 / 연산자는 나눗셈이 아니라 경로를 결하(join)하는 연산자..
    #macos, linux , windows 마다 경로구분자가 다른데.. 이를 알아서 해줌.

    with client.audio.speech.with_streaming_response.create(
        model='gpt-4o-mini-tts' , # 제일 쌈
        voice='ballad',  # https://www.openai.fm/ 에서 목소리를 들어볼 수 있음
        input= '안녕하세요. 저는 AI 비서입니다.',
        instructions='밝고 친절한 톤으로 말해',
    ) as response:
        #응답결과에 바이트로 온다는것.
        response.stream_to_file(audio_file_path)



def ai_stt():
    #실시간 음성 인식으로 정확한 텍스트 변환 Speech to Text

    #구글 검색 : openai stt api
    # https://developers.openai.com/api/docs/guides/speech-to-text

    #가격 
    #1. whisper-1 : 분당 $0.006 
    #2. gpt-4o-transcribe : 분당 $0.006 (오디오 입력 기준)
    #3. gpt-4o-mini-transcribe : 분당 $0.003  텍스트 출력 1M토큰당 $5.00


    #1. .env 에 있는 api-key 읽어오기
    from dotenv import load_dotenv
    load_dotenv()


    from openai import OpenAI
    from pathlib import Path
    client = OpenAI()

    #01예제에서 만든 음성파일 읽어서 글씨로 보여주기
    audio_file_path = Path(__file__).parent / 'myspeech.mp3'


    #03예제에서 녹음한 음성파일 읽어서 글씨로 보여주기
    # audio_file_path = Path(__file__).parent / 'recorded_audio.wav'


    #경로의 오디오 파일을 읽어오기 (바이너리로..)
    audio_file = open(audio_file_path,'rb')

    #이진수 덩어리
    #ai에게 오디오데이터를 주고 글씨를 응답받기
    transcript = client.audio.transcriptions.create(    # transcript :녹취록 
        model= 'gpt-4o-mini-transcribe',
        file=audio_file, #오디오 데이터 바이트 덩어리...
        response_format='text'  # json으로 하면 메타까지 포함됨. 

    ) 

    #추출된 글씨를 출력
    print(transcript) # 회의록 저장을 이렇게 함. 실제 실무용

def audio_recording():
    #streamlit 스트림릿에서 오디오를 입력받는 방법

    import streamlit as st
    st.title('음성 녹음을 테스트합니다')

    #사용자로부터 오디오를 입력받는 기능
    audio_data = st.audio_input('마이크를 대고 말씀하세요')

    #녹음된 오디오 데이터가 있는지 확인
    if audio_data is not None:
        st.success('녹음이 완료되었습니다. !')
        #오디오 재생
        # st.audio(audio_data,format='audio/mp3') # streamlit은 무조건 .wav만 가능 , 
        st.audio(audio_data,format='audio/wav') # streamlit은 무조건 .wav만 가능

        #파일에 저장
        with open('recorded_audio.wav','wb') as f:
            f.write(audio_data.getvalue())

        st.write('파일 저장 완료: recorded_audio.wav')
        st.write(audio_data.type)





################ main() #####################
def main():

    # streamlit_GPT_interaction()
    # ai_tts()    
    #ai_stt()
    audio_recording()

    # my_chatbot_test1()
    # streamlit_each_feature()
    # streamlit_sidebar_feature()
    # streamlit_feature2()
    
    # streamlit_alert_message()
    # text_expressoin_on_streamlit()
    # markdown_expression()
    # markdown_caption('2026 plan for badminton')
    # markdown_code('Hello world','python')
    # markdown_code('document.write("Hello JavaScript")','javascript')
    # st.divider()

        

    



if __name__ == "__main__":
    main()
