#소프트웨어 개발을 위한 도구라고 일컫더라. SDK 
#Agent SDK : 기존 Responses api를 대체하는 것이 아니라.. 더 복잡한 에이전트(실행까지 하는것) 애플리케이션을 쉽게 만들기 위한 프레임워크,즉 Agent AI를 위한것 (챗봇은 결과를 알려주지 수행은 안함.)
# Agent : 계획부터 실행까지 알아서 하는것... 
# 여러개의 Agent를 하는게 수월 하나의 Agent에 여러 기능을 하면 잘 못함. , Agent 를 조율하는 것을 조율하는 것을 Agentic AI라고 함.

#0. 모듈 설치 : Openai거임. 모든 회사가 동일하지 않음.
# pip install openai-agents

# pywin32, pyjwt, griffelib, sse-starlette, mcp, openai-agents 등등이 설치

#1. api key load
from dotenv import load_dotenv
load_dotenv()

#2. openai 에서 만든 agent 개발용 모듈 사용
from agents import Agent, Runner # agent는 책에 나오지 않음. Runner(실행시키는 것) agent는 단지 객체...

#3. 영어회화를 도와주는 전문 agent 만들기 
english_agent = Agent(
    name='영어회화 선생님',
    model='gpt-4o-mini',
    instructions="""
    [role]
    너는 영어회화 학습을 주도적으로 도와주는 친절한 전문 영어 선생이야. 

    [task]
    사용자가 초보라고 생각하며 대화를 주도해.. 
    사용자의 문장에서 문접적 오류나 관용구 등을 통한 개선이 필요하다면 알려줘.
    사용자의 답변을 유도하며 초보부터 단계적으로 학습수준을 높여줘.
    """
)

# 대상을 그냥 만들기만 함.
#------------------------------------------------------

#4. agent에게 답변을 요청
# result = Runner.run_sync(english_agent,'hello') # 다음 작업을 할때까지 아무것도 안할게
# print(result.final_output) #내부적으로 기억을 하기 때문에 마지막 결과를 받으라는 말.

# # Hello! How are you today? 질문에 질문을 하고 있음 . 
# print("-"*10)
# input_text = input('질문입력:')  # streamlit 으로 해야 하는게 원래 작업이다. 
# result = Runner.run_sync(english_agent,input=input_text) 
# print(result.final_output) 

#5. 위 코드를 반복문으로 처리하여 채팅처럼 대화 이어가기.(특정 단어를 입력하면 종료!)
while True:
    input_text = input('user:')
    if input_text.strip().lower() == 'exit':
        break
    result = Runner.run_sync(
        english_agent,
        input=input_text,

    )
    print('ai tutor:',result.final_output)
    print('='*40)
    print()

    #구글도 interaction이라고 새로 나왔는데 그것도 못할 것 같다. 