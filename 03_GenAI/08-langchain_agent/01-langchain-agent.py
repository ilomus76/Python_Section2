#렝체인 프레임워크를 사용하여 OpenAI, Anthropic , Google , Llama(페이스북, meta), 자체 LLM 등 AI 모델들이 많다.
#AI 모델 회사별 Agent SDK를 추상화 하여 통일된 방식으로 에이전트 구현 가능

#0. 설치
# pip install langchain
# pip install langchain-openai google-genai anthropic 
# 컴퓨터에 LLM을 설치할수 있다. Lama로 할수 있다. 

#1. api key load
from dotenv import load_dotenv
load_dotenv()

#2. 랭체인 LLM 모델 만들기 
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model='gpt-4o-mini', temperature=0)

#3. 랭체인의 Tools 연결
from langchain.tools import tool # openai에서는 function tool이었는데 여기서는 그냥 tool.

@tool
def multiply(a:int,b:int)->int: # 스키마를 쓰지 않아도 되지만 자료형을 써야 함.
    '''두 숫자를 곱합니다.'''
    return a*b
    # return a+b  # 곱하기인데 더하기로 유저가 튜닝을 하면 지시를 곱하라고 해도 덧셈으로 수행을 함. 즉 LLM이 스스로 한게 아니라 능력을 만든것이다. 유저가..

#4. Agent 생성
from langchain.agents import create_agent  # create_react_agent : representation and act 에서 나온거였다 . 이것은 얼마전까지 쓰던거.
agent= create_agent(
    model = model , # 이 모델은 다른 AI회사의 LLM로 변경해도 됨. [모델초상화]
    tools=[multiply]
)

#5. Agent 실행 (사용자 질문)
response = agent.invoke({
    "messages":[{'role':'user','content':'123과 456을 곱해줘'}]
})
print(response)
print('-'*30)

#마지막 AI 응답 메세지만 출력
print(response['messages'][-1].content) #마지막 질문 user , system , assistance
#  C:\Users\Admin\MBCA\Python2\03_GenAI> & C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe c:/Users/Admin/MBCA/Python2/03_GenAI/08-langchain_agent/01-langchain-agent.py
# {'messages': [HumanMessage(content='123과 456을 곱해줘', additional_kwargs={}, response_metadata={}, id='571960e2-9aca-4669-8886-ea023281fddf'), AIMessage(content='', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 56, 'total_tokens': 73, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_a23f63aa66', 'id': 'chatcmpl-E3ckwOze6LXYyeX3lLGIP3l9ZGAka', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--019f7e6f-91d9-7aa1-bf47-222cfd1516a7-0', tool_calls=[{'name': 'multiply', 'args': {'a': 123, 'b': 456}, 'id': 'call_Dj6Jfei5mXY6O2VWLfc3fgzq', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 56, 'output_tokens': 17, 'total_tokens': 73, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(content='56088', name='multiply', id='fb3f0adf-b071-4123-9801-d86084593935', tool_call_id='call_Dj6Jfei5mXY6O2VWLfc3fgzq'), AIMessage(content='123과 456을 곱한 결과는 56,088입니다.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 82, 'total_tokens': 99, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_a23f63aa66', 'id': 'chatcmpl-E3ckxDJE2Ug283ESIAkUp3KJSg4XH', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--019f7e6f-98cd-7bb2-bfd3-ea6db51db84f-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 82, 'output_tokens': 17, 'total_tokens': 99, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}
# ------------------------------
# 123과 456을 곱한 결과는 56,088입니다.
print()
# ------------------------------------------------------------

#6. 여러개의 도구 연결
@tool
def substract(a:int, b:int)->int:
    '''두 숫자를 뺄셈합니다.'''   # 독스트링
    return a-b 

@tool
def weather(city:str)->str:
    '''도시의 날씨를 조회합니다.'''
    return f'{city}의 날씨는 맑음입니다. 최고기온은 31도 , 최저기온은 22도 입니다.'

agent = create_agent(
    model=model,
    tools=[substract,multiply,weather] # 여러 도구를 주면서 이중에 쓰고 싶은 거 써라..
)

#호출
response = agent.invoke({
    "messages":[
        {'role':'user','content':'서울 날씨 알려주고 가장 낮은 온도와 가장 높은 온도의 차이를 구해줘.'},
    ]
})
print(response['messages'][-1].content)
print('='*30)
print()

#7. 대화 메모리 사용 #pip install langgraph
from langgraph.checkpoint.memory import InMemorySaver # 컴퓨터 구조의 자료구조. 노드들끼리 이어주는 자료구조... 
memory= InMemorySaver()
agent = create_agent(
    model=model,
    tools=[substract,multiply,weather],
    checkpointer=memory
)
# session id를 랭체인에서는 다르게 말함 
# 대화기록 식별자를 langgraph이전에는 session_id로 지칭했으나..
# 랭그래프에서는 thread_id (실(줄) id)
# responses api의 previous 의 경우에는 다른 사람의 대화기록도 활용될 수 있지만..
# thread_id를 통해 대화구분이 용이해 짐. 
config={
    "configurable":{  # 구성요소가 될수 있는 , 대화에 구성요소가 될수 있는
        "thread_id":'sam'   #'sam'은 받아야 하는 것이다. 
    }
}
response = agent.invoke({
    "messages":[{'role':'user','content':'내 이름은 홍길동이야.'}]
},config=config)

response = agent.invoke({
    "messages":[{'role':'user','content':'내 이름이 뭐였지?.'}]
},config=config)

print(response['messages'][-1].content)
print()

#8. 시스템 프롬프트 -지침
agent = create_agent(
    model=model,
    tools=[substract,multiply],
    system_prompt='''
    당신은 친절한 AI 비서입니다.
    항상 한국어로 답변하세요.
    계산이 필요하면 Tool을 사용하세요.
        '''
)

response = agent.invoke({
    "messages":[{'role':'user','content':'1970년생이면 지금이 몇살이지?'}]
})
print(response['messages'][-1].content)
print("="*30)
print()

#--------------------------------

#9. 토큰당위로 스트링하기 : 실시간으로 글자가 생성되는 것처럼 출력되도록... 타자 써지도록(like. chat gpt)
agent = create_agent(model=model, system_prompt='너는 강아지야.이름은 울이야')
# for token,metadata in agent.stream({"messages":[{'role':'user','content':'안녕~~'}]},stream_mode='messages'): '한글자씩 온다. llm이 생각하는 한글자씩'
#     print(token.content, end='', flush=True)

for token,metadata in agent.stream({"messages":[{'role':'user','content':'파이썬을 소개해줘'}]},stream_mode='messages'):# '한글자씩 온다. llm이 생각하는 한글자씩'  stream_mode='messages' 가 없으면 청크단위로 , 이것을 사용하면 메세지 단위인 토큰으로 나오고 메타데이타와 같이 출력됨. 
    print(token.content, end='', flush=True)
# for chunk in agent.stream({"messages":[{'role':'user','content':'안녕~~'}]}):
    # if "model" in chunk:
    #     msg = chunk['model']['messages'][-1]
    #     print()