# LCEL [LangChain Expression Language] : 랭체인에서 체인을 구성하기 위한 표현 언어
# 핵심 아이디어는 각각의 수행하는 녀석들을 Runable(각 도구들. 작업수행자들) 들을 파이프(|)로 연결 
# 원래 | 는 : 의 위/아래를 연결한 것

# 총 3개의 runnable 을 연결해보기 (prompt-model-출력파서)

# 0. api key 
from dotenv import load_dotenv
load_dotenv()

#1. 체인으로 구성할 구성요소들(runnable들) import 
# from langchain_core.prompts import PromptTemplate           # 프롬프트 탬플리 
from langchain_core.prompts import ChatPromptTemplate          # 프롬프트 탬플리 
from langchain_openai import ChatOpenAI                     # LLM (두뇌역할)
from langchain_core.output_parsers import StrOutputParser   # 출력파서 : 종류는 많아서 구글링 해서 찾아봐라

#1) 프롬프트 탬플릿 
prompt = ChatPromptTemplate.from_template(
    "다음 문자을 영어로 번역하세요:{text}"
)

#2) LLM 모델
model = ChatOpenAI(model='gpt-4o-mini')

#3) 출력파서 - 응답을 일반 문자열로...
parser = StrOutputParser()  

# 여기까지 총 3개의 runnable를 만든 것이다.

# 이제 묶자
# (핵심) 랭체인의 체이닝 기법(순서 중요~ 파이프라인 구축) : 입력 -> prompt -> LLM -> output parser ->최종 문자열
chain = prompt | model | parser  # 연결끝

# 요청 및 응답
response =chain.invoke({'text':'안녕하세요'})
print(response)
print('-'*30)
#출력파서의 종류는 아주 많음. 검색해봐

from langchain_core.output_parsers import JsonOutputParser
parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_template('''

다음 문장을 JSON으로 출력하세요.
                                          
문장 : {text}

반드시 아래 형식으로만 출력하세요.
{{"message:":"<문장>"}} # 안은 Javascript
'''
)

chain = prompt | model | parser
response = chain.invoke({'text':'나는 홍길동 입니다.'})
print(response)

#############################
# [수행1] part8 유투브 요약/번역 서비스
# [수행2] part9 이미지생성 동화 AI 구현 