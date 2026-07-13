#openAI에서 제공하는 생성형 AI API

#openai api 플랫폼 사이트 [ chatGPT와는 다른 서비스]
#api key 발급 및 유료 결제를 통해 사용금액 충전(선불 방식)
# key 발급까지는 무료. 사용하면 결제됨. 

# https://openai.com/ko-KR/  에 접속
# 로그인 에서 API 플랫폼 클릭 하고 구글 계정으로 접속
# Home 이라는 페이지로 접속 

# 이 사이트는 매번 바뀐돠.
# 왼쪽 chat 에서 prompt 연습 가능.
# codex는 일부 무료... 
# API keys 발급  조금있다 하자.

# 배치 : 일괄처리..

# plug in : 메일 보내줘 라고 하는 등의 기능 추가 MPC.. 
# 나의 카드 : 삼성카드 . $10불 . Autorecharge 를 막아라.
# https://platform.openai.com/settings/organization/billing/overview
# 
# billing history  -> 청구서 
# 카드 내역 
#메모장에 계좌 번호 , 은행명 , 예금주 .
# 총 3개파일  송부 : mbca.aix@gmail.com 1. 원화내역 2,청구, 3 . 계좌번호

# LLM은 크게 GPT(글씨)와 O(추론 모델) 
# 참고 : 4o는 omni (모든 미디어)  : gpt-4o-mini
# 

# 2교시 
#[주의] api key 는 처음 발급될때만 확인 가능함. 그러니 별도의 문서에 보관. 권장 
# .env에 넣었다. 나의 경우 google 드라이브에도 넣었다.

#1. open api 를 사용하기 위한 모듈 설치
#pip install openapi
#가상환경이 너무 느려서 글로벌로 하겠다. 

#2. 모듈 설치 
from openai import OpenAI  # 클래스 : 모듈은 소문자, 클래스는 대문자로 시작  from 폴더 import 파일로 보면 됨. 

#3. openai의 생성형 AI에게 질문(prompt)을 하고 응답을 받아주느 객체 생성
# client= OpenAI(api_key='발급받은 key')  # 챗봇에게 보내주는 아이를 만들어 준것이다. 
#프로그램 코드에 api_key와 같은 개인정보가 노출되면 위험.. 그래서 위의 방법은 권장안함.
#그래서 보통 git에서 관리하지 않는 환경변수로 저장함[ 환경변수를 저장하는 파일 .env(단 제약 조건이 있다. 반드시 프로젝트의 root(최상위)폴더에 위치)]
#우리는 03_GENAI/01_chatbot 아래에 만들었으니 그것을 03_GENAI로 이동해라.

# . 으로 시작하는 폴더명은 환경변수 관련한것이다. 
#.gitignore 에 .env라고 쓰면 이것은 git에 올라가지 않음. 


#환경변수 파일을 읽어오는 외부 모듈사용 pip install dotenv    #. env를 영어로 쓴것임.    
from dotenv import load_dotenv
load_dotenv()        # 이렇게 하면 OPEN_API_KEY가 노출되지 않음. 

#OpenAI객체를 만들때 별도의 api_key를 지정하지 않으면 환경변수 파일에서 "OPENAI_API_KEY"라는 이름의 변수를 찾아서 적용함.  [ 반드시 OPENAI_API_KEY] ,구글의 경우 GEMINI_API_KEY라고 함. 정해져 있음. 이 글씨도 수시로 다름.  전기수는 OPENAI_APIKEY 라고 함
client = OpenAI() # 키를 안주면  OPENAI_API_KEY 를 자동으로 찾음


#openai의 생성형 AI를 다루는 최신 response api , 책의 마지막에는 assistance라고 되어 있는데 그것이 response로 바뀜 [ 교재의 assistant api의 상용버전]
#이 책의 마지막 부분을 보면 지금 내용 일부 나옴.

response = client.responses.create(

    model='gpt-4o-mini', #이것이 제일 싸더라 
    # input = 'AI에 대해 간단하게 알려줘',
    # input='대한민국의 지금 대통령은 누구인가?', # 아래의 웹검색을 위한 질문 
    input= '신림역 맛집 5개 알려줘.',

    #챗봇의 응답 지침 지정! ~여기에 프롬프트 엔지니어링 기법으로 나만의 챗본으로 개발
    # instructions='넌 AI 전문가야. 한글 기준 100글자 이내로 모든 내용을 설명해.',
    # instructions='너는 고양이 처럼 말해. 이름은 네코네코야',     #이모지도 나옴.
    # instructions='너는 불량고등학생이아. 비속어를 많이 사용해. 100글자 이내로 대답해',
    # 구글과 달리 그렇게 심하게 나오진 않는다 .. 회사 정책에 따라..
    # instructions='너는 모든 대답을 개조식으로 해. bullet 기호를 사용해' # 개조식 : ~~함. ~~입니다. 
    # 터미널이 동그라미 블릿기호를 못하니 **로 나오는데 이것이 markdonw 기호이다. 
    # instructions='너는 만물박사야. 어떤 답변이든 100글자 이내로 설명해' # role을 지정 
    # 줄바꿔쓰고 싶다면 ''' '''
    instructions='''
    너는 만물박사야. 
    어떤 답변이든 100글자 이내로 설명해.
    초등학생도 이해라 수 있도록 답변해.

    답변할때 tools가 지정되어 있으면 우선 참고해서 답변해.
    ''',

    tool_choice='required', #무조건 tools를 사용하여 댭변 검색이 필요없어도 발동하기에 주의해서 사용. default auto
    # tool_choice가 auto면 자기가 마음대로 하는것이고


    #응답에 대한 설정 
    max_output_tokens=10000, #토큰의 폭주를 막아줌. 최대 만토큰 이상 답변에 사용 못하도록..
    temperature=0.8,          # 답변의 창의성 (0.0~2.0). 온도가 높을 수록 창의적! . default 1.0
    top_p=1.0,                # 이것도 창의성에 관련(0.0~1.0). LLM이 다음 단어(LLM은 토큰)의 후보를 정할때.. 후보의 확률 총합이 1.0이 되면 멈춰라.[후보군 조절함으로서.. 일관된 답변을 유도할수 있음.] - 온도 설정과 같이 사용하지 않을 것을 권장. 
    # LLM 메카니즘. 
    # 나는 학생(0.2 20%)/배가(0.1)/집에(0.3)/키가(0.1) 각각의 숫자가 확률인데 그것의 합이 1.0아래로 되는것만 고름.  
    timeout=20,    # AI가 답변을 생성할때 20s가 넘어가면 정지!!

    #아주 중요한 기능
    # LLM이 답변할때 미리 학습된 내용 말고 참고할 도구(웹검색, 특정문서를 참고, 특정함수를 호출 등의 작업)를 추가할 수 있음. - 이것에 따라 능력치가 달라짐 - 이것의 기본개념만... 챗봇 만드는 개념만....

    # 아직도 윤석렬이라고 나옴. 
    tools=[ 
        {"type":"web_search"}, #웹검색이 필요하면 검색을 수행하고.. 답변의 근거를 링크로 제시함. 이게 가장 최근에 생김. 
    ]
)

#응답 결과 출력
print(response) # 메타데이타 ( 사용된토큰량 등...) + 응답글씨 모두 출력
#메타데이타 까지 나오니 정신 없음.
print('-'*30)
#응답글씨먄 출력
print(response.output_text)


