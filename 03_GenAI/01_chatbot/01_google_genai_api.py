#genai 가 모듈 이름

# Google AI studio에서 제공하는 LLM 생성형 API 활용 ( Open AI 는 유료여서 지금은 구글것 사용)

# https://aistudio.google.com
# https://aistudio.google.com/welcome?utm_source=google&utm_medium=cpc&utm_campaign=Cloud-SS-DR-AIS-FY26-global-gsem-1713578&utm_content=text-ad&utm_term=KW_google%20ai%20studio&gad_source=1&gad_campaignid=23417416052&gbraid=0AAAAACn9t66Fzby66f5XLcMtV8TftkBG6&gclid=Cj0KCQjwjb3SBhDgARIsAMKiWzgotWrYxpGXaXOUmWaCOdY6g4uisWC_JzVdlep2b5ZFNy18TKqi8YwaAt0HEALw_wcB

#######################################################################
# 가격에 사용되는 단위인 token 에 대한 의미!
# [open ai 토큰계산기 ] : https://platform.openai.com/tokenizer
# [google ai studio 토큰 이해 및 계산 ] : https://ai.google.dev/gemini-api/docs/tokens?hl=ko&lang=python


# Gemini 3.5 Flash  : 겉의 이름
# gemini-3.5-flash  : 코드에서의 이름


# 프럼프트 엔지니어링
# 컨텍스트 엔지니어링 : 문맥에 따라 답변 
# 하네스 엔지니어랑 : 

# Gemini 3.1 Flash-Lite
# gemini-3.1-flash-lite

# Gemini Omni Flash 프리뷰
# gemini-omni-flash-preview

# Gemini 3.1 Pro 프리뷰
# gemini-3.1-pro-preview 및 gemini-3.1-pro-preview-customtools
###########################################################################

# 가격 정책 확인 : 무료로 사용가능한 모델드리 일부 존재함. [실습활용]

# 개발 가이드 문서를 참고하여 개발(업데이트 자주 되니 주기적으로로 확인)

# https://ai.google.dev/gemini-api/docs?hl=ko  # 다큐먼테이션 


# https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko&_gl=1*1jj6uck*_up*MQ..*_ga*MTA2ODkzNzU4NS4xNzgzNjUzMTQw*_ga_P1DBVKWT6V*czE3ODM2NTMxMzkkbzEkZzAkdDE3ODM2NTM0MjgkajYwJGwwJGg0MTcwMjAxOTE.



## https://aistudio.google.com/welcome?utm_source=google&utm_medium=cpc&utm_campaign=Cloud-SS-DR-AIS-FY26-global-gsem-1713578&utm_content=text-ad&utm_term=KW_google%20ai%20studio&gad_source=1&gad_campaignid=23417416052&gbraid=0AAAAACn9t66Fzby66f5XLcMtV8TftkBG6&gclid=Cj0KCQjwjb3SBhDgARIsAMKiWzgotWrYxpGXaXOUmWaCOdY6g4uisWC_JzVdlep2b5ZFNy18TKqi8YwaAt0HEALw_wcB
#여기 개발자 사이트 와서 get started 버튼을 눌러 접속해서 로그인
#왼쪽 아래에 자시 게정 있으면 됨 

#playground 에서 연습 할수 있음. 


# 1. 키발급. 
# 
# 2. google genai 모듈 설치 

# pip install -q -U google-genai   -q : 조용히 해 ... 글씨 막 보여 준다... -U 있으면 설치 안하고 없으면 설치  -q 를 하니 터미널에서 반응이 안보임. 
# 가상환경 없이 그냥 글로벌로 하자.


#3. 모듈 사용 
from google import genai


#4. LLM 사용을 요청하는 객체 생성 
client = genai.Client(api_key='GOOGLE_API_KEY')  #https://aistudio.google.com/api-keys



# 8. 모델이 응답할때 참고(사용)할 도구 주는 함수..
#1) 대한민국 대통령의 정보를 리턴해주는 함수(ai model 답변을 할때 사용할 함수를 결정할때 doc string을 참고한다.)
def get_president_korea():
    """
    doc string:
    이 함수는 대한민국 대통령에 대한 질문을 답변하기 위해 사용됩니다.
    """
    #실제로는 이 데이터를 네이버 검색. 뉴스검색 api를 이용하여 가져와서 반환
    # system_instruction='너는 불량한 고등학생이야. 답변도 비속어를 섞어서 해', 라고 하고 ai한테 질문을 하니 이재명이 return이 안되고 기분 나쁜 불량한 태도로 윤석열이라고 대답하는 경우가 있었음. 내 생각으로는 LLM이 자기가 내부적으로 불량한 정도로 답하기 위해서 답을 하면서 return 윤석열 스럽게 하면서 break를 명령을 쓴것같음.
    return "이재명"

def get_weather():
    #기상청 open api 를 통해 날씨 데이터를 가져오기
    import requests
    weather = requests.get('기상청 open api.json') ## 실제 open api 작업할것이
    return weather

#7. 모델이 답변하는 내용을 조정하는 설정객체를 생성
from google.genai import types
config=types.GenerateContentConfig(
    max_output_tokens=500, #생성될 응답의 최대 토큰 수를 제한합니다. 이렇게 하면 저 글자 이상은 안함. 이것을 넘어가면 자동으로 정지
    # temperature=2.0,  # 생성된 응답의 무작위성 제어함. 창의력을 조절(0~2.0) 기본 1.0 .. 온도가 높을 수록 열정적인 모델..창의적. 그래서 말하는 대답이 말안되게 나옴. 독특한 답변하려고 함.
    # temperature=0, # 냉소적.. 창의성 결여.
    # top_p=0.5,          # 확률의 p , 이것도 창의성과 관련.. 모델이 다음 토큰을 선택할때 고려하는 후보군의 확률 총합이 0.5가 되면 후보 선정 완료 [ 일관성 있는 답변을 유도할때 많이 사용 , top_p가 좀더 일관성 있게 함.]
    # 생성형 을 이해해야 함. 글자 하나하나를 완성해 나가는 과정, nice to meey you라면 첫번째 nice라고 쓰면 그 후 나올수 있는 후보군을 본다. nice world 는 0.3 30% , nice to 0.2 nice phone 0.1 
    # top=k 는 이것을 몇개까지 만들레  .. 그리고 그 다음 나올것의 확률을 만듦. 후보군들 중에서 확률이 높은것을 줌. 하지만 이것이 똑같으면 항상 또 일정하게 나오니 이것도 확률로 랜덤하게 나오게
    # top=k 를 20으로 하면 후보군 20개중 , 또는 p로 하면 후보군들 중 0.5 합이 안되게 그리고 그 아웃풋을 셀프 어텐션기능으로 만들어냄. 이 단어 다음 다음 단어 가 나오는데 그 후보군을 정하는것이 top_p이고 top_k는 적게 그리고 
    # 이것이 랜덤하게 선택되게 함. 그리고 셀프 어텐션을 이용해 다음 단어 선택

    # response_mime_type='text/plain',   #'text/plain' 기본값 
    # response_mime_type='application/json',    #요청에 대한 결과값을 json으로 줌 , 이런 식으로 하면 반환 글자가 적어서 토큰수가 줄어들 수 있다.

    # seed=42,
    # 랜덤 기능은 파이썬이 할수 없다 . 시간이 지나서 어떤 값을 선택. seed 값을 고정하면 어떤 값을 항상 같은 값을 갖게 됨. 
    # 랜덤 테이블가짐. 특정 seed가 있으면 어떤 시간까지 거리가 같아 같은 값을 갖게 됨. seed는 시간을 가지고 함. seed를 0 혹은 42를 많이 씀. 
    # 그래서 후보군들 중에서 랜덤하게 선택될때 .. 랜덤값을 일관되게 생성 - 매번 같은 응답(숫자는 아무 숫자나)
    # 42를 쓰는 이유는 1970년대 히치하이커 소설에서 인생이 뭐야 할때 42라고 썼음... 이진수로 42가 1010 의 이진수... 전자가 충돌해서 반사되는 각도가 42도. 설은 많음. 이것은 의미가 없고 min 같은 의미


    #시스템에게 응답 지침을 미리 설정. 
    #이것에 따라서 모델은 같은데 완전 다른 결과가 나옴.
    # system_instruction='너는 고양이야 이름은 네코에코야', #프럼프트 엔지니어링  
    system_instruction='너는 불량한 고등학생이야. 답변도 비속어를 섞어서 해',

    #나만의 챗봇을 만든것이다. 페르소냐를 만든것이다. 롤을 만든것이다. 

    #우리가 만든 것을 튜닝할 수 있다. 

    #미리 학습한 것 외에도 답변하도록 하기 위해 모델에게 추가도구를 주기!  대통령이 누구냐 물었는데 지금 이재명이 아니라 윤석렬이 나오는 것을 없애기 위해
    # 오픈 북을 주는 것임
    # tools=[함수명1, 함수명2]
    # tools=[get_president_korea],  # 모델에게 도구를 주는 것이다. 오늘 배움의 목적...

    #햔개가 아니라 여러개도 만들수 있다.
    tools=[get_president_korea,get_weather],  # 모델에게 도구를 주는 것이다. 오늘 배움의 목적...


    #우리의 목적은 이것을 이용하여 생성형 api 앱을 만드는 것이다. 

)

#5. 요청하기 : requests와 비슷 
response = client.models.generate_content( # 텍스트를 생성해주는 함수 , 응답이 옴
    model='gemini-3.5-flash', # 정해져 있는 키워드가 있음 #실습은 무료등급이 지원되는 모델 중 선택. 무료사용량을 소진하면 모델 변경   시작하기 -> 가격정책 -> 
    # model 의 가격 정책이 끝나면 다른 것으로 바꿔라. 하지만 가격이 쉐어 되는게 있다. 
    # model='gemini-omni-flash-preview',
    # model='gemini-2.5-flash',
    # 이때 다른 계정을 사용하면 또 될수도 있음. 키를 바꿔야 한다. 
    # contents= "너는 구글 제미나이야? 아님 chatGPT야?", #사용자의 프롬프트 (질문)
    contents= "대한민국의 대통령은?",


    #답면을 조정하는 설정(설정이 여러개이기 때문에 설정객체를 통해 지정) 
    config= config,
)
#6. 응답결과 출력
print(response)  # token 사용낵 등. 메타데이타와 응답.메타데이터와 응답 글씨를 가지고 있음.  # ai는 답변을 확률적으로 하기 때문에 같은 질문이라도 다른 답을 하는게 정상. 
print(response.text)

# 이제 내 프로그램에서 AI API 를 사용할 수 있다라는 것을 알수 있다.






