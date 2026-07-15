#LLM은 이전 대화내용을 기억하지 못함. LLM에게 이전 대화의 history르 인식하도록 연결

#0. api key 적용

from dotenv import load_dotenv
load_dotenv()


#1. 필요한 모듈 import 및 openai 모델 생성
from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    temperature=1 ,#0.1,
    max_completion_tokens=5000,
    model='gpt-4o-mini',    
    
    )

#2. langchain 랭체인 model 에게 질문 및 응답
question = '안드레이 카파시가 누구인지 설명해주세요'  # 이분이 vibe라는 말을 탄생시킨 사람
response = model.invoke(question)  # invoke 혹은 stream 사용
print(response.content)


#3. 랭체인은 프롬프트를 조금 더 자세하고 규격화하여 작성하기 편하도록(프롬프트엔지니어링과 연관) 프롬프트 탬플릿을 만들어 적용할 수 있음 . import 필요
from langchain_core.prompts import PromptTemplate
prompt_tample='{who}가 누구인지 설명해주세요'
prompt = PromptTemplate(template=prompt_tample,input_variables=['who']) # who를 변수처럼 받아드림. 

#완성된 프롬프트 확인하기 
# print( prompt.format(who='안드레이 카파시'))
# print( prompt.format(who='이순신장군'))


#.format()으로 직접 프롬프트를 완성하고 요청하는 것도 짜증.
# 이 프롬프트 탬플릿과 모델을 체인으로 연결하면.. 응답을 요청할때 알아서 탬플릿을 참고하여
# 프롬프트를 완성한 후 응답해줌. 

# chatbot_chain = prompt | model  #파이프라인처럼 연결됨 (or 연산자로 연결됨) - 순서틀리면 안됨. # |(or 연산자) 연산자는 LCEL 언어임. 별도 수업. # prompt는 여기서 템플릿임
# response = chatbot_chain.invoke({'who':'제프리 힌튼'}) #이미지 영상쪽에서 큰 영향
# print(response.content)
# print('--'*20)


#이전 대화를 기억하는지 확인  -> 결과 : 이전의 대화를 기억하지 못하는 것다.
# response=chatbot_chain.invoke('그(그들)이 현재 어디서 살고 있나?')
# print(response.content)
# print('--'*20)


#이전 대화를 기억하도록 구현해 보기 -- 탭플릿에 이적ㄴ 기록들이 표시되도록

#(이전까지의 대화기록 history)과 (현재 사용자 질문 input)을 같이 알수 있도록 프롬프트 탬플릿 만들기 
prompt_temlate = '''
아래는 사람과 AI의 대화기록입니다. AI 이름은 MBCA 친구보십니다. 
대화문맥을 바탕으로 친절하고 간결한 답변을 진행하세요.

현재 대화:
{history}

사람:{input}
AI: 
'''

#프롬프트 완성 ~변수명 2개 지정
prompt= PromptTemplate(template=prompt_temlate, input_variables=['history','input'])

#모델과 템플릿을 체인으로 연결
chatbot = prompt | model 

# prompt 의 {history}에 대화기록을 남기려면 메세지 단위로 관리해야 함. 메세지 단위의 대화기록을 관리하는 클래스 ChatMessageHistory 임 ( humanmessage처럼)
# 이 클래스를 사용하기 위해 langchain의 하위모듈 community 를 설치 pip install langchain-community ( 책에서는 pip install langchain_community 와 같이 언더바로 되어 있음 )
from langchain_community.chat_message_histories import ChatMessageHistory


# 단 , 이 앱을 사용하는 사용자가 여러명이면 chatbot 이 어떤 사용자의 대화기록인지 구별 안됨. 
#실제 챗봇드링 대화기록을 구별하기 위해 [세션 session(연결)] 이라는 개념을 사용
# 
# # 개념을 이해해 보면..
# #1. 사용자 A가 챗봇과 대화를 시직하면 세션1이 됨
#2. 동시에 사용자 B가 챗봇과 대화를 또 시작하면 세션 2가 됨
# # 즉, 챗봇은 세션 ID를 기반으로 대화기록을 구별하여 답변을 생성함. 

# 사용자들의 세션과 ChatMessageHistory 객체를 저장할 dictionary를 생성
session_messages ={} # 빈 딕션너리 {key(세션ID):value(ChatMessageHistory)}

#세션 ID를 부여하는 여러방법
#1. UUID 를 생성하여 session_id를 생성 [ Unique Identifier UUID : 범용 고유 식별자 -- 고유한 식별자를 만들어 사용]
#2. 이미 사용자 고유 ID가 존재하고 있다면 이를 사용 ( 회원번호 같은것)
#3. 타임스탬프 사용 . (사진 저장할때 처럼...)  : 나 하나가 세션이 여러개일수도 있다. 나갔다가 다시 접속할수도 있기 때문에..

# 실습목적으로 간단하게 미리 session_id를 고정
session_id = 'sam'   # 내 프로그램으로 시작하면 sam으로 시작한다..

# 혹시 기존에 session_messages로 등록된 id가 있는지 확인

if session_id not in session_messages:
    # session_messages[session_id]=채팅 메세지기록 #ChatMessageHistory
    session_messages[session_id]=ChatMessageHistory()

#대화기록 session_messages를 chatbot(model+prompt : 기억을 못함)와 연동되어 응답하도록.. 메모리 챗봇만들기
#메모리와 chatbot을 연동해주는 클래스 사용
from langchain_core.runnables.history import RunnableWithMessageHistory
chatbot_memory = RunnableWithMessageHistory(
    chatbot, 
    # 함수의 주소를 받는 변수 에 lambda 함수로 전달 , 변수를 session_id를 
    get_session_history= lambda session_id:session_messages[session_id],  # lambda 함수 ( 자바스크립트의 화살표합수 같은 것)
    input_messages_key='input',
    history_messages_key='history'
)


# 이전 대화를 기억하는 챗봇에게 질문하고 답변받아보기
response = chatbot_memory.invoke({'input':'BTS가 누구인지 설명해줘'},config={'configurable':{'session_id':session_id}})
print(response.content)
print('='*30)
print()

response = chatbot_memory.invoke({'input':'빌보드에서 1등한 곡들은?'},config={'configurable':{'session_id':session_id}})
print(response.content)

# LangChainDeprecationWarning: RunnableWithMessageHistory is deprecated. Use LangGraph's built-in persistence instead.
# session id 를 알려주기 위해서 설명함. 

# 안드레이 카파시(Andrej Karpathy)는 인공지능(AI) 및 머신러닝 분야의 저명한 연구자이자 엔지니어입니다. 그는 특히 딥러닝과 컴퓨터 비전 분야에서의 기여로 잘 알려져 있습니다. 카파시는 스탠포드 대학교에서 박사 학위를 받았으며, 그의 연구는 주로 신경망, 자율주행차, 그리고 이미지 및 비디오 처리와 관련된 주제에 집중되어 있습니다.
# 그는 또한 테슬라(Tesla)에서 AI 및 자율주행차 관련 프로젝트를 이끌었던 경험이 있으며, 이곳에서 딥러닝 기술을 활용하여 자율주행 시스템을 개발하는 데 중요한 역할을 했습니다. 카파시는 또한 OpenAI에서 연구원으로 활동한 경력이 있으며, 머신러닝 교육 자료와 강의로도 유명합니다.
# 그의 블로그와 강의는 많은 사람들에게 영감을 주었으며, AI와 머신러닝 분야의 발전에 기여하고 있습니다.