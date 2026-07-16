# 오픈소스는 훈련을 시켜야 한다 이것은 나중에
# 지금은 훈련된 것을 사용하자

# openai 에서 제공하는 임베딩 모듈 사용 
# 나중에 RAG를 구축하기 위해 Langchain 프레임워크 모듈과 함께 사용 
# RAG는 LLM 모델의 프롬프트로 제공하기 위한 방법임


# 0 필요한 모듈 설치 
# pip install langchain : 터미널에서 설치해라..
# pip install langchain-openai 

# 1.임베딩 모델 import
# 설치는  langchain-openai
from langchain_openai import OpenAIEmbeddings
#이것은 api key가 필요함 

#2. api key 불러오기
from dotenv import load_dotenv
load_dotenv() # api key는 코드상에 노출시키지 않아도 불러옴

#3. 임베딩을 해주는 객체 생성
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002') #  : 책에서 하는 모델 , 긴토큰 처리 가능    , text-embedding-3: 성능이 떨어짐.

#[임베딩 테스트] 텍스트를 주고 임베딩 요청 --숫자로 된 벡터값으로 만들어 주세요~~
# 돈나가기 때문에 주석처리
# result = embeddings.embed_query('저는 배가 고파요')
# print(result) # 벡터값 확인 가능 [-0.01663736067712307, -0.02178889885544777, 0.015218060463666916,.....]
#------------------------

#4. 여러개의 문장을 가진 데이타 준비(RAG에서는 chunk들)
data = [
    '저는 배가 고파요',
    '저기 배가 지나가네요',
    '굶어서 허기가 지네요',
    '허기워기라는 게임이 매우 재밌어',
    '스팀에서 재밌는 거 해야지',
    '스팀에어프라이어로 연어구이 해먹을거야'
]

#데이타의 출력을 보기좋게 panda라는 표형태(데이터프레임)의 데이터를 다루는 모듈을 사용
import pandas as pd
df = pd.DataFrame(data,columns=['TEXT'])
# print(df)

#TEXT컴룸만 가진 df에 새로운 컬룸을 추가하고 그 값들로 글씨의 벡터값을 저장
vector_data=[]
for text in data:
    vector_data.append(embeddings.embed_query(text))  # embeddings를 사용할때 돈이 나감.

df['VECTOR'] = vector_data # 새로운 'VECTOR'컬룸을 만들고 데이터들을 대입해줌.  # 내생각 : pandas에서 보면 열에 해당하는 배열이지만 의미적으로 1차원 배열인 리스트를 갖는 데이타 하나를 대입할수 가 있구나...
print(df)
# 벡터값 확인함. 
print('='*30)
print()

# [구현] 벡터값을 이용하여 사용자가 입력한 어떤 문장과 가장 유사도가 높은 상위 3문장 뽑아내기
#1)유사도 계산 함수 만들기
import numpy as np
from numpy import dot #내적 계산에 필요
from numpy.linalg import norm

#함수 한줄로 만들어봐라
def con_sim(A,B):
    return dot(A,B)/(norm(A)*norm(B))

#2) 전달받은 글씨와 가장 유사도가 높은 문장을 dataframe에서 찾아서 유사도값이 높은 상위 3개만 리턴하는 함수 만들기.
# 참고 실제로  dataframe이 글씨와 벡터값을 가지고 있는데 이게 실제 DB의 모습이다.

def get_similarity_top3(df,query): # 벡터DB , 사용자 요청 
    # 사용자 요청질문을 임베딩하기
    vector_query = embeddings.embed_query(query)

    # 문자들의 벡터값을 가진 데이터프레임(df)의 각 줄마다 위 사용자 요청글씨 벡터값과의 유사도 구하기 
    similarities = []
    for i in range(len(df)): # 0,1, 2 ,, 즉 데이터 프레임의 개수만큼
        #현재번째 줄의 벡터값
        vector = df.iloc[i]['VECTOR'] # iloc[i] i번째의 줄의 .. 즉 엑셀의 i번째열의 "vector"칸을 가져옴

        #벡터의 수학적 계산을 위해 넘파일 배열로 만들기
        A = np.array(vector_query) #사용자 질문
        B = np.array(vector)   # 현재번째 문장
        similarities.append(con_sim(A,B))
    #--------------for 문 끝

    # 구해진 유사도 값들을 데이터프레임의 새로운 컬룸을 만들어 저장
    df['SIMILARITY']=similarities

    #유사도 높은 top3만 추출 
    top3 = df.sort_values('SIMILARITY',ascending=False).head(3) # df를 sort 해 주세요  ""의 값을 기준으로  # ascending 이 오름차순 , .head(3): 머리에서 3개
    return top3
#--------------------------------------------------------------------------


#[사용하기]사용자의 특정 질문과 가장 유사한 문장을 찾기
result = get_similarity_top3(df=df,query='아무것도 안 먹었더니 꼬르륵 소리가 나네')
print(result)