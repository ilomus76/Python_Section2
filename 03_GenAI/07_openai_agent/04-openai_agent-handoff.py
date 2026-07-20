#여러 Agent를 조율하여 최종 목적을 달성하도록 하는 에이전틱 AI 개발에 용이한 기능

#예제 : 수학 Agent와 역사 Agent 
from dotenv import load_dotenv
load_dotenv()

from agents import Agent,Runner

#1) 수학 Agent
math_agent = Agent(
    name = '수학 선생님',
    model='gpt-4o-mini', # 수학 선생님은 이 모델 , 영어선생님은 다른 모델을 써도 됨
    instructions='''수학문제를 해결하는 전문가입니다.'''
)

#2) 역사 Agent
history_agent = Agent(
    name = '역사 선생님',
    model='gpt-4o-mini', # 역사 선생님은 이 모델 , 영어선생님은 다른 모델을 써도 됨
    instructions='''역사 질문에 답하는 전문가입니다.''',
)

#문제 해결에 적절한 agent를 조절하는 라우터용 Agent..즉, 여러 Agent를 오케스트레이션(혹은 슈퍼바이저:랭체인에서는 슈퍼바이저라고 함) 하는 메인 Agent 
router = Agent(
    name='감독 에이전트',
    model='gpt-4o-mini',
    instructions='''
    질문을 보고 적절한 전문가에게 전달하세요.
    두 전문가의 지식이 모두 필요하다면 한 에이전트의 결과를 다른 에이전트가 입력으로 받아 대답해줘.
    두 전문가의 지식이 아닌 '모르는 분야입니다. 저는 역사/수학 에이전트입니다.'라고 응답해.

    [제한사항]
    markdown 문법을 사용하지 말것. **이 싫어서.. 
    ''',
    handoffs=[math_agent,history_agent]
)

#(실습)
# result = Runner.run_sync(router,'세종대왕은 누구인가?') #역사 agent가 답해야 할것이다. 
# print(result.final_output)
# print('-'*30)

# result = Runner.run_sync(router,'표준점수는 어떻게 구하는가?') #수학 agent가 답해야 할것이다. 
# print(result.final_output)
# print('-'*30)

# result = Runner.run_sync(router,'조선이 건국된지 올해로 몇 년이 되었나요?') #수학 ,역사 agent가 답해야 할것이다. 
# print(result.final_output)
# print('-'*30)

result = Runner.run_sync(router,'3박 4일 일본 여행일정을 계획해줘?') #이것은 아무런 전문 agent가 없다. 
print(result.final_output)
print('-'*30)

#이건 openai거인데 이제 우리는 추상화를 알고 있으니 랭체인으로 agent를 만들어 보는 것을 해보자.
#실제 현업에서는 openai것만 사용하는 것이 아니다 그래서 랭체인을 사용.