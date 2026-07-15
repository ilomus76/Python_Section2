# 랭체인 프레임워크 - 생성형 AI 웹앱 개발을 용이하게 해 주는 AI용 프레임워 마치 react 와 비슷. 

# * 기본적으로 LLM 모델(OpenAI, Google, Anthropic)마다 구현코드가 일부 다름. 하지만 랭체인을 사용하면 모델을 변경해도 코드의 큰 변화 없이 동작이 가능함(이것을 모델 추상화)

# 나의 생각 : LLM 이 자기가 알아서 외부 API 에 접속해서 결과를 알려주는 기능이 Agent 이고 , 이 LLM 들이 어느곳을 돌아다니면서 기억을 하면 모든 접속하는 곳을 이용해서 컴퓨팅을 할수 있으니 커다란 컴퓨터를 만들수 있을 듯.
#         : 여기에 메모리를 달기 위해 추가되는 장치가 HBF 임. session_state로는 용량이 되지 않음.


# [4교시]

# 1. 필요한 모듈 설치 
# 랭체인 : LLM을 이용한 어플리케이션을 만들기 위한 core 모듈. pip install langchain 
# 이것만 있으면 안됨. 회사마다 접속 방법이 다름 
# 랭체인 OpenAI : OpenAI 모델(GPT)을 랭체인과 연결해주는 모듈 pip install langchain-openai     : 참고 GPT 이외의 추론을 담당하는 모댈 O로 시작  
# 랭체인 Google : Google 모델(제미나이)을 랭체인과 연결해주는 모듈 pip install langchain-google-genai  
# 랭체인 Anthropic : Anthropic 모델(소넷,오퍼시,미토스)을 랭체인과 연결해주는 모듈 pip install langchain-anthropic  

# 03_GENAI>pip install langchain 

#책에서는 _로 설치하는데 지금은 - 로 함.

#2. 설치 끝. 다음으로 API KEY 환경변수에 등록하고 Model 객체 생성하기 - .env 에 등록 
#.evn 파일에 환경변수로 key를 저장할때 변수명 : GEMINI_API_KEY  - Langchain에서는 GOOGLE_API_KEY
from dotenv import load_dotenv
load_dotenv()

#OpenAI
from langchain_openai import ChatOpenAI  # 예가 생성형 AI
model = ChatOpenAI( model='gpt-4o-mini',temperature=1, max_completion_tokens=10000) # instruction은 없음 . 이것은 다르게 넣음.

#Google
from langchain_google_genai import ChatGoogleGenerativeAI
model_google= ChatGoogleGenerativeAI(model='gemini-3-flash-preview') # temperature도 가능

#Anthropic (클로드) 도 동일


#3. 모델에세 질의하고 응답받기  -- 아래것은 할때마다 돈들어 가니 주석처리 하자...
# response = model.invoke('랭체인이 무지?') # 모델아 발동해라..
# print(response)
# print('-'*30)
#--------------------------------------------

#모델에게 지침을 주고 싶다면... 사용자의 발화인지. 시스템의 메세지인지 구별할 수  있어야 함.
# 이것은 지금 우리가 쓰는 것보다 더 오래것이고 예전에는 메세지에 지침이 있다고 생각했었음 . 어제까지의 기술은 가장 최신의 간편한 방법이었음. 
# 랭체인에서는 3종류의 메세지 클래스 제공함


#4. 메세지 종류 
#HumanMessage  사용자의 발화를 담는 메세지 클래스   {'role':'user','content':'..'} , 예전에는 이 딕션너리를 만들지 않았기 때문에 이것을 HumanMessage로 만든것임.
#AIMessage    LLM의 응답을 담는 메세지 클래스    {'role':'assistant','content':'..'}
#SystemMessage 시스템 세세지 클래스 (지침 or 역할)  {'role':'system','content':'..'}

#위의 3개를 쓰고 싶으면 라이브러리를 가져와야 함. 아래.
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
system_message = SystemMessage(content='너는 랭체인 테스트를 위한 챗봇이야. 모든 질문의 답을 한 문장으로 간단하게 요약해서 대답해')   
# instruction 은 가장 최근에 나온 기능이고 role 도 누구는 user, 누구는 assitant ,, 그래서 저 딕션너리를 하나로 만들어 주는 것

ai_message = AIMessage(content='무어이든 물어보세요. 한문장으로 설명해 줄게요.')
user_message = HumanMessage(content='안녕?랭체인이 뭐지' )

#모델에게 입력하기 위해 리스트로 만들기 
messages = []
messages.append(system_message) # 지침  # 지침 있을때
messages.append(user_message)        # 지침없을때

#모델에게 메세지를 전달하고 응답하기 
#지침없이 와 지침있을때 
response = model.invoke(messages)
print(response.content)

#google model에 메세지를 전달하고 응답받기
response2 = model_google.invoke(messages)
print(response2.content)

#LLM이 응답이 모두 완료될때 까지 .. 는 화면에 아무것도 표시되지 않음.
#모델이 데이터를 조금씩 생성할때 마다 바로바로 출력해서 마치. 타자써지듯 구현 가능
# stream 기능