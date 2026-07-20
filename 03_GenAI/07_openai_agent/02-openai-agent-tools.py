# openai agent sdk + 도구(함수호출) 결합

from dotenv import load_dotenv
load_dotenv()

from agents import Agent,Runner, function_tool # 객체, 객체, 함수 

#도구(LLM이 답변할 도구 , web search file search function)로 사용할 함수 만들기 --데코레이션 @

#데코레이션 @
@function_tool    
def get_weather(city:str)->str:  #파라미터와 리턴값을 자료형을 명시 . # 화살표 함수 , string을 city로 받고 답변을 str으로 준다라는 표현
    """도시의 날씨를 조회합니다."""
    return f"{city}의 현재 날씨는 맑음, 27도 입니다"  # 실제로는 여기에 우리가 구현한 기능들이 추가되어야 함. 
#함수 도구는 여러개 일 수 있음.
@function_tool
def get_exchange_rate() ->str:
    '''USD /KRW 환율을 조회합니다.'''
    import requests
    r = requests.get('https://') # 여기에 주소를 주면 자기가 줌. 
    return r.text

#DB 정보 읽어오는 기능합수
@function_tool
# def search_customer(name:str, amount:int )->int or any:
def search_customer(name:str, amount:int )->str:
    '''
    고객 정보를 조회합니다.

    # 함수 스키마
    Args:
    name: 검색할 고객 이름
    amount : 계좌 정보 
    '''
    #DB 조회
    return f'{name}고객님은 VIP 회원입니다.'
#1.agent 만들기
agent =Agent(
    name ="Weather Agent",
    model='gpt-4o-mini',
    instructions='''
    사용자가 날씨를 물어보면 get_weather 도구를 사용합니다.
    ''',

    tools=[get_weather],
)

# 대화가 기록이 되지 않더라... 이것도 가능할텐데 대화를 리스트로 기록하던지 해야 할듯 하다. 
# 요즘에는 graph라는 것이 뜨고 있어서.. 그것은 구조가 좀 다름. 
result =Runner.run_sync(agent,'서울 날씨 알려줘')
print(result.final_output)