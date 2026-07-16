#LLM 모델들은 정해진 입력 길이를 넘어가는 텍스트는 한번에 검토할수 없음.(이 텍트트의 총량을 [context Window]라고 부름. 문맥창)

# opneai에서는 8000토큰까지 context window 가능

# RAG 시스템을 구현할 때는 긴 글을 알정단위로 쪼개야 함. 
# 이 쪼개진 단위를 Chunk(청크)라고 부름.
# 이 청크를 어떻게 나누느냐에 따라 RAG 품질이 달라짐. 실험적으로 구현해야 함. 

# 시나리오별 권장 청크 사이즈 
# 강사님 경험상 
# A. 한국어 문단 RAG : 350정도 
# B. FAQ/고객센터 : 200토큰 이내.
# C. 문서         : 250~300 tokens
# D. 법률 등등은 다른데.. 이정도만.

# 긴 글을 잘라서 청크를 만들기
#1 . RecursiveCharacterTextSplitter(글자 길이 기준) ---- [권장] : 현업에서 많이 사용. 
#2 . SemanticChunker               (의미 기준) ~ 느림.. 대용량 문서에서는 비효율적

#1] 긴 텍스트를 읽어보기 
with open('./05_langchain_rag/2016-10-20.txt','r',encoding='utf-8') as f:
    texts=f.read()
print('텍스트의 길이:',len(texts))  #18085369 글자수 


#2] 글씨를 일정 길이 이상 되지 않도록 잘라서 청크를 만들기 # 참고로 책에 있는거 그대로 하면 안됨. 책대로 하지 말고 
from langchain_text_splitters import RecursiveCharacterTextSplitter #책에서는 text_spliter로 했음.
#청크를 만드느 객체 생성
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=0) # 청크끼리 의미가 잘리는 경우가 있음
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100) # 청크간의 겹치는 부분의 사이즈를 정함.
#overlap : 청크들의 글씨들을 겹치게 하는 정도 
# (통상 10%~20% - 청크가 500이면 50~100)

#분할을 할때 무조건 같은 사이즈로 나눠지는 것은 아님. 500은 기준이 될뿐이다.
#분할기가 자를때 기준 ( \n\n 먼저 짜름, \n, 공백문자:띄어쓰기되면 자름) 문자를 기준으로 자름. 그러다 500글자 이상되면 강제로 도중에 잘라버림

#3] 
#여기서 chunk의 최대길이는 500임
# chunks = text_splitter.create_documents([texts,text2]) 
chunks = text_splitter.create_documents([texts]) # 한개의 문서로만 하자
print('분할된 청크의 개수:',len(chunks))  # chuncks : 47068개


#5] 분할된 청크들 확인해보기 : 청크는 항상 똑같이 나오지 않음.
print('-'*30)
# print(chunks[0])
print(chunks[0].page_content) # 글씨만 보이게

print('-'*30)
# print(chunks[1])
print(chunks[1].page_content)

print('-'*30)
print(chunks[2].page_content)

print('-'*30)
print(chunks[3].page_content)


#------------


# 보통 이런 문서들은 회사에서 사용하는 문서들이어서..txt보다는 pdf,xmls,hwp형태가 많음.
#xlsx는 우리가 많이 해서 pdf로 하자.