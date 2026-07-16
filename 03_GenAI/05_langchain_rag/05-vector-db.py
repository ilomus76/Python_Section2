#벡터값을 체계저긍로 저장하는 벡터 DB중 유명한 오픈소스(돈안내고 쓰는 , 돈내고 쓰려면 파이픈) 3개
# 1. Chroma ( 크로마) : 처음 다루기 용이. 대규모에는 적합하지 않음. python하고 잘 맞음. 회사에서는 Javascript로도 할수 있다 .. python 모든것들이 javascript로도 변환이 다 되어 있다.
# 2. Faiss (파이스) : 검색 속도 빠름. GPU사용. 대규모 용이. / DB라기 보다는 검색엔진에 가까움. CRUD, 메타데이터를 직접 구현해야 함. 처음시작하는 입자에서 버거움. 
# 3. Milvus (밀버스) : 완전한 벡터 DB. 분산저장. 수억~수십억 벡터 지원/ 설치와 운영이 복잡. 리소스 요구량이 큼. 
# 4. 파인콤 . 클라우드에서 관리. 규모작은곳에서 좋은 선택지..

#[실습 - Chroma] - pip install langchain-chroma
#RAG 서비스를 위한 벡터DB 저장 워크플로 구상하기 ----
#1. 데이터 준비 - RAG에 사용할 PDF 문서를 읽어와서 LLM이 처리할수 있는 단위(청크 Chunk) 로 자르기(chunk) : pyPDFloader , RecursiveCharacterTextSpliter , 자르는 것은 실험적으로 해야 함.
#2. 청크들(문장들)을 벡터값으로 입베딩 : OpneAIEmbeddings [ 비용발생]
#3. chroma 벡터 DB에 저장하고 질문에 대해 유사도가 높은 문장 추출 : chroma가 다 알아서 해줌. [ 벡터DB는 유사도를 자동으로 구해주는게 역할임. 이전것은 이해하기 위한 실습용이었음]
# -------------------------------------------------------------------
# 

#1. PDF 파일을 읽어와서 적절한 크기로 잘라 chunk 만들기 -> 이 주석을 AI한테 주면 고대로 만들어 줌
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader= PyPDFLoader('./05_langchain_rag/2023_북한인권보고서.pdf')
docs = loader.load() # 요즘 회사에서 사용하는 방법  -> 페이지 단위로 읽음.
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100) # 100은 500의 20%
chunks = splitter.split_documents(docs)

print(len(chunks))
print('-'*20)
print()

#2. 청크들을 벡터값을 만들어주는 임베딩 객체 준비(api key 필요)
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002') # 모델에 따라 성능이 다름. 
#벡터값을 만드는 작업은 직접하지 않고 .. 벡터DB를 만들때 임베딩 객체를 주면 알아서 벡터화 진행함

#3. 벡터 DB 만들기 
from langchain_chroma import Chroma
db = Chroma.from_documents(chunks,embedding=embeddings) #문서를 준것이다. 그리고 임베딩 객체도 줌. #이때 돈!!들어감. 
print('저장된 문서의 갯수:',db._collection.count()) #RDBMS : 표처럼 생긴 Database  , Node SQL : No SQL [노드구조]- 각 아이템마다 갯수를 달리할수 있고 다시 생성할수 있다. 여기서 board를 collection일라고 함.
# No-SQL 방식... _collection(컬렉션 : RDBMS의 테이블같은 역할)

# Node SQL 예시
# board - d1-
#           -
#           -
#     - d2
#     -d3 

print('-'*30)

#벡터 DB가 만들어 졌다.. 

#[벡터 DB 사용]
#1)사용자의 특정 질문에 대한 답변을 위해 검색할 유사도가 높은 문장들 찾기

question= '북한의 교육과정'   
#LLM은 학습이 안되어 있고 잘못된 정보를 가지고 있음. 
docs = db.similarity_search(query=question) #여기서 가장 근접한 문장 찾아줌.
print(f'{question}과 유사한 문서의 개수:',len(docs))

#각 문장들이 무엇인지 확인해보기
for doc in docs: #문장 마다 찍어보자
    print(doc)
    print('-'*20)
#-------------------------------------

#2) 상위 3개의 문서로만 제한하고 유사도 점수도 같이 확인해 보기
top3_docs = db.similarity_search_with_relevance_scores(question, k=3) # top3만 나옴.
for doc in top3_docs:
    print(doc)
    print('-'*20)

#------------------------------------------------------------

#4. 벡터 DB를 만들때 영구적으로 데이터를 저장하여 재사용하는  것이 효율적
#1) chroma vector db에 청크들을 저장하면서 .db 파일로 저장하기
db1=Chroma.from_documents(chunks,embedding=embeddings,persist_directory='./05_langchain_rag/chroma_test.db') # 내부적으로 폴더 구조임. # chroma_test.db 는 파일이 아니라 디렉토리임.  여기는 돈들어감.
print('벡터로 잘 저장되었습니다. 문서갯수 :',db1._collection.count())
print() 
#2) 저장되어 있는 .db로 부터 크로마 벡터 DB객체 생성하여 사용하기.
db2=Chroma(persist_directory='./05_langchain_rag/chroma_test.db',embedding_function=embeddings) #이것은 돈들어 가지 않음. 

print('파일에서 읽어온 DB의 문서갯수:', db2._collection.count())

question = '북한의 군 복무기간'
docs = db2.similarity_search_with_relevance_scores(query=question,k=3) 
for doc in docs:
    print(doc)

#동작이 잘 안되서 강사님거랑 비교해 봐라.