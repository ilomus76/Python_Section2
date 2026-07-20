#구글도 interaction으로 업데이트
# open_response 도 오픈 ai의 최신 것이다.

#역사 수업같은것이다.


# openai 의 3가지 api 비교

# 0. api key load
# 외부 모듈 , 설치필요
from dotenv import load_dotenv
load_dotenv()

#1. Completions API : 가장 초기 방식 . 사용자 입력과 지침을 구별하지 않고 입력

# 이것을 바뀌지 않음.
from openai import OpenAI
client = OpenAI()

#처음에 하던 방법
completion = client.completions.create(
    model='gpt-3.5-turbo-instruct',   # 그당시 사용하던것
    prompt='너는 인공지는 전문가야. 인공지능의 미래에 대해 간략히 설명해 주세요',  # 질문[인공지능의 미래에 대해 간략히 설명해 주세요]과 프롬프트[너는 인공지는 전문가야.]를 같이 있는 느낌
    temperature=0.7,
    max_tokens=150,
)

# print(completion.choice[0].text)  # 여러개의 초이스를 주고 선택해서 쓰게.. 
print(completion.choices[0].text.strip())  # 여러개의 초이스를 주고 선택해서 쓰게.. 위아래 공백이 많아서 그것을 없애주는 기능 추가.
print('-'*30)
print()

#2. Chat Completions API : 표준인터페이스
#특징 : 메세지별 역할을 구분하는 개념이 등장. ("system","user","assistant")
completion = client.chat.completions.create(    # 책이 전부 chat 으로 하는 이 방법을 사용
    model='gpt-4o-mini', # 이때부터 구분하기 시작함. 
    messages = [
        {'role':'system','content':'당신은 AI 전문가입니다.'}, # 내가 쓰는것은 시스템 지침서이다. 
        {'role':'user'  ,'content':'머신러닝과 딥러닝의 차이점을 설명해 주세요'},
        # {'role':'assistant'  ,'content':'머신러닝과 딥러닝의 차이점을 설명해 주세요'},  # 대화를 기록하기 위해서 ... 

    ],
    temperature=0.7,
    max_completion_tokens=200,

)
print(completion.choices[0].message.content)
print('-'*30)
print()

# 결과 
# 1. **정의**: 머신러닝은 데이터로부터 학습하여 예측이나 결정을 내리는 알고리즘을 개발하는 분야입니다. 머신러닝 모델은 주어진 데이터를 기반으로 패턴을 인식하고, 이를 통해 새로운 데이터에 대한 예측을 수행합니다.
# 2. **알고리즘**: 머신러닝에는 다양한 알고리즘이 있습니다. 예를 들어, 선형 회귀, 로지스틱 회귀, 의사결정 트리, 서포트 벡터 머신(SVM), K-최근접 이웃(KNN) 등이 있습니다.
# 3. **특징**: 머신러닝 모델은 일반적으로 데이터 전처리와 특징 공학(feature engineering)에 많은 의존성을 가집니다


#3. response API : 차세대 에이전트형 인터페이스 - 2025년에 등장
#대화 상태를 유지하는 기능도 포함. 외부 도구와 연결(연동)이 용이.

#첫번째 요청
response1 = client.responses.create(
    model='gpt-4o-mini',
    instructions='너는 한국어 AI 전문가입니다.',
    input='최근 인공지능 기술 트렌드를 알려줘', 
    # 이 전까지는 자기가 학습한것으로만 결과를 주었지만 이때부터 외부 도구를 사용할 수 있게 됨.
    tools=[{'type':'web_search'}], # 웹 검색 도구 활성화
)
print(response1.output_text)
print('~'*10)

response2 = client.responses.create(
    model='gpt-4o-mini',
    instructions='너는 한국어 AI 전문가입니다.',
    input= ' 이 중에서 가장 주목받는 기술은 무엇이야?',
    #이전 응답기록을 인식하도록.. 이전 응답의 식별아이디를 지정 (아래)
    previous_response_id=response1.id
)
print(response2.output_text)

#결과 답변을 보면 근거를 준다. 
# 3. **푸드테크 분야의 AI 적용**: 식품 산업에서도 AI 기술이 적극적으로 활용되고 있습니다. 미국에서 열린 CES 2023에서는 AI와 데이터 분석 기술을 기반으로 한 식품 산업의 혁신적인 제품들이 소개되었습니다. ([v.daum.net](https://v.daum.net/v/20230121091221072?utm_source=openai))
# 4. **로봇 산업의 기술 개발과 시장 전망**: 로봇 산업에서는 AI와 머신러닝 기술을 활용한 로봇 개발이 활발히 진행되고 있습니다. 이러한 기술들은 제조업, 의료, 서비스 등 다양한 분야에서 로봇의 활용도를 높이고 있습니다. ([yes24.com](https://www.yes24.com/product/goods/121576054?utm_source=openai))
# 5. **재무회계 분야의 AI 도입**: 재무회계 분야에서도 AI와 머신러닝 기술이 도입되어 업무 효율성을 높이고 있습니다. 이러한 기술들은 인재 유지, 회계 자동화, 기업 가치 창출 등에 중요한 역할을 하고 있습니다. ([blog.workday.com](https://blog.workday.com/ko-kr/3-trends-will-reshape-accounting-finance-2023.html?utm_source=openai))


#gpt-4o-mini : 멀티모달 

# 구글에서 openai response api 라고 검색하면 나온다. 
