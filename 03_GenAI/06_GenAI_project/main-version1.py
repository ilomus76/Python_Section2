# Comment 
# All of this project is made based on the 06-rag-chatbot.py to study ranchain of RAG.


########################## 내부 기능함수 #########################################33
import hashlib

def get_file_hash(filename):
    sha = hashlib.sha256()

    with open(filename, "rb") as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            sha.update(data)

    return sha.hexdigest()

#######################################################
####           The file name : main.py
#######################################################
# workflow 





if __name__ =="__main__":
    print('This is created on the virtual environment')
    print('Start of Langchain project')




    # pip install streamlit
    # streamlit : Streamlit은 항상 처음부터 다시 실행됩니다. 이벤트가 발생할 때마다 화면을 다시 그려야 합니다.
    # 그래서 Streamlit은 이벤트가 발생하면 스크립트 전체를 처음부터 다시 실행합니다

    # HTML 
    import streamlit as st

    if "upload_key" not in st.session_state:
        st.session_state.upload_key = 0
    
    print("session_state:",st.session_state.upload_key)
    st.write("session_state:",st.session_state.upload_key) 



    filename = None

    # --------------------------
    # 1. 로컬 파일
    # --------------------------

    uploaded = st.file_uploader(
    "문서를 선택하세요",
    type=["pdf", "txt", "csv", "json", "xml", "xlsx", "xls"],
    key=f"upload_{st.session_state.upload_key}"
    ) 

    if uploaded:
        #객체의 속성값을 보는 함수 
        print(dir(uploaded))
        st.write(dir(uploaded))    

        # 객체를 그림으로 이해하기
        # uploaded
        #         │
        #         ▼
        # +--------------------------------------+
        # | UploadedFile 객체                    |
        # |--------------------------------------|
        # | name  = "example.pdf"                |
        # | type  = "application/pdf"            |
        # | size  = 152340                       |
        # |--------------------------------------|
        # | read()                               |
        # | getbuffer()                          |
        # | seek()                               |
        # | tell()                               |
        # +--------------------------------------+
        # uploaded.name → 파일 이름(속성)
        # uploaded.type → MIME 타입(속성)
        # uploaded.size → 파일 크기(속성)
        # uploaded.getbuffer() → 파일 내용을 바이트로 가져오는 메서드
        # uploaded.read() → 파일 내용을 읽는 메서드



        filename = uploaded.name 
        with open(filename, "wb") as f:
            f.write(uploaded.getbuffer())

        print(uploaded.name)
        st.write("file name:",uploaded.name)
    print(uploaded)
    st.write("file name:",uploaded)



    # --------------------------
    # 2. URL
    # --------------------------

    import requests
    import webbrowser

    if st.button("브라우저 열기"):
        webbrowser.open("https://www.google.com")
        #https://www.emva.org/wp-content/uploads/EMVA1288Linear_4.0Release.pdf

    # url = st.text_input("문서 URL")
    url = st.text_input("또는 문서의 URL을 입력하세요")

    if uploaded is not None:
        st.success(f"업로드한 파일 : {uploaded.name}")

    elif url:
        try:
            #pip install requests
            response = requests.get(url)

            if response.status_code == 200:

                filename = url.split("/")[-1]
                with open(filename, "wb") as f:
                    f.write(response.content)

                st.success(f"{filename} 다운로드 완료")
                st.success("URL에서 파일을 읽었습니다.")
                st.write("파일 크기 :", len(response.content), "bytes")
            else:
                st.error("URL에서 파일을 다운로드하지 못했습니다.")

        except Exception as e:
            st.error(e)
    else:
        print('파일 혹은 URL 아무런 파일도 로드되지 않았습니다.')
        st.write('파일 혹은 URL 아무런 파일도 로드되지 않았습니다.')



    # WORK #1 [구성요소1] 검색기(리트리버 )만들기 
    # To make/create/build the retrieving site as retriever 



    # Load pdf/xlsx/hwp/text/json/csv/xml file that I want to use for vector embedding

    # 내 컴퓨터에서 파일 선택하기(가장 많이 사용) ⭐⭐⭐⭐⭐  : tkinter 
    # 웹(인터넷 URL)에서 읽기
    # Streamlit에서 업로드하기(AI 챗봇에서 가장 많이 사용)
    # Gradio에서 업로드하기 



    import os

    # 파일이 선택되지 않은 상태에서 다음 코드 실행 방지
    if filename is None:
        st.warning("파일을 업로드하거나 URL을 입력하세요.")
        st.stop()



    ext = os.path.splitext(filename)[1].lower() 
    # return 값으로 파일명과 확장자가 튜플로 출력되는데 파일명이 [0], 확장자가 [1]
    print('file extenstion:',ext)
    st.write('file extension:',ext)

    if ext == ".pdf":

        # from langchain_community.document_loaders import PyPDFLoader

        
        ###################################################
        ###  pdf 읽어오는 준비 과정 
        ###################################################
        # python의 pdf 리더 모듈 중 3대장 
        # PDF는 겉으로 보기에는 하나의 문서처럼 보이지만, 컴퓨터 입장에서는 글자, 그림, 표, 선, 좌표 등이 복잡하게 저장된 파일입니다. 그래서 PDF를 읽으려면 전문 라이브러리가 필요합니다.
        # pip install pypdf      : 기본 모듈 , PDF 파일을 읽고, 합치고, 나누고, 회전시키는 등의 작업을 하는 라이브러리
        # pip install pymupdf    : pdf를 다루는 다향한 기능이 추가된 모듈 , PDF를 매우 빠르게 읽는 라이브러리입니다. 텍스트뿐 아니라 이미지 그림 도형 좌표까지 모두 다룰 수 있습니다.
        # pip install pdfplumber : pdf에서 표, 텍스트, 비텍스트 요소를 구분하여 추출해주는 모듈
        # pip install pypdf pymupdf pdfplumber 라고 하면 3가지가 다 설치됨

        print("Opening ",filename)
        st.write("Opening ",filename)
        from langchain_community.document_loaders import PyPDFLoader
        
        loader = PyPDFLoader(filename) # 파일이름을 불러와서 객체 생성 
        #pdf_loader = PyPDFLoader('./05_langchain_rag/2020_경제금융용어 700선_게시.pdf')  # 금융용어 설명해주는 챗봇 만들겠다
        docs = loader.load()
        print('읽은 문서의 총 페이지 개수:',len(docs)) #페이지로 되어 있음.  #PDF 문서에서 필요없는 페이지를 제거하는 정제작업 필요.. 우리는 시간이 없지만 실제로 제거해야 한다. 필요없는 페이지를 ...예를 들면 맨뒤 발행년도등은 문서내용과 상관이 없어 제거해야 함.
        st.write('읽은 문서의 총 페이지 개수:',len(docs))


        #####################################################
        #### langchain 
        #####################################################
        # pip install langchain
        # pip install langchain-community
        # pip install langchain-openai
        # pip install langchain-text-splitters
        # pip install langchain langchain-core langchain-community
        
        # langchain-core: LangChain의 핵심 기능(엔진)
        # langchain: 체인, 에이전트 등 AI 애플리케이션의 기본 기능
        # langchain-community: PDF, 웹, 데이터베이스, 벡터DB 등 외부 서비스와 연결하는 다양한 도구 모음
        # langchain-openai: OpenAI 모델(GPT 등)과 연결하는 전용 라이브러리
        # langchain : 차의 차체에 해당 주요 기능 Chain Agent Memory
        # langchain-core : 차의 엔진 : 가장 중요한 핵심 기능입니다.예를 들어 Prompt Runnable Message OutputParser 등이 들어 있습니다. 자동차로 비유하면 엔진 
        # langchain_text_splitters : RecursiveCharacterTextSplitter
        # pip install langchain-community : 랭체인과 pdf loader 모듈 연결해주는 모듈, 여러 외부 프로그램을 연결합니다.

        
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        # document_splitter =RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        # chunks = document_splitter.split_documents(docs) 
        # chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100).split_documents(docs)
        chunks = RecursiveCharacterTextSplitter(
                chunk_size=500, 
                chunk_overlap=100,
                separators=[
                "\n# ",
                "\n## ",
                "\n### ",
                "\n\n",
                "\n",
                " ",
                ""
                            ]
            
            ).split_documents(docs) 
        # penAI API 비용이 발생하지 않습니다.
        # 비용이 발생하는 것은 LLM이나 임베딩 모델(API)을 호출할 때입니다

        # 직접 커스텀 Splitter 만들기 : 예] ParagraphRecursiveTextSplitter라는 클래스 , overlap을 하지 않고 바로 문단을 나누기 위해서
        # class MyTextSplitter(RecursiveCharacterTextSplitter):
        # ...
            
        print('문서내의 총 청크(chunk)의 갯수',len(chunks))
        st.write('문서내의 총 청크(chunk)의 갯수',len(chunks))


        # 논문 : 공식 관련 
        # 기술문서 : 용어 

    elif ext == ".csv":
        print("Opening ",filename)
        st.write("Opening ",filename)
        from langchain_community.document_loaders import CSVLoader
        loader = CSVLoader(filename)

    elif ext == ".txt":
        print("Opening ",filename)
        st.write("Opening ",filename)
        from langchain_community.document_loaders import TextLoader
        loader = TextLoader(
            filename,
            autodetect_encoding=True
        )

    elif ext == ".json":
        print("Opening ",filename)
        st.write("Opening ",filename)
        from langchain_community.document_loaders import JSONLoader
        loader = JSONLoader(
            file_path=filename,
            jq_schema=".",
            text_content=False
        )

    elif ext in [".xlsx", ".xls"]:
        #there in no way to load xlsx and xls
        #instead of loading xlsx and xls, use pandas like as below.


        print("Opening ",filename)
        st.write("Opening ",filename)

        #pip install pandas
        import pandas as pd
        from langchain_community.document_loaders import DataFrameLoader
        df = pd.read_excel(filename)

        loader = DataFrameLoader(
            df,
            page_content_column=df.columns[0]
        )

    else:
        raise ValueError(f"지원하지 않는 파일 형식입니다 : {ext}")


    #####################################################
    #### Vector Embedding :  
    #####################################################
    #벡터DB
    #pip install langchain_chroma
    #pip install langchain_openai
    #pip install langchain_openai langchain_chroma 
    
    from langchain_chroma import Chroma
    from langchain_openai import OpenAIEmbeddings
    from dotenv import load_dotenv
    load_dotenv()

    #for streamlit
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        api_key = st.secrets["OPENAI_API_KEY"]


    if api_key is None:
        st.error("OPENAI_API_KEY가 설정되어 있지 않습니다.")
        st.stop()


    webbrowser.open("https://www.openai.com")
    # total usage : $0.69 / $10.00 untl July 18
    # embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
    embeddings = OpenAIEmbeddings(model='text-embedding-ada-002',api_key=api_key) 
    # embeddings = OpenAIEmbeddings(model="text-embedding-3-small",api_key=api_key)
    #정확히는 "객체를 생성하는 것"은 비용이 없고, "임베딩을 생성하는 순간" 비용이 발생합니다.





    #####################################################
    #### Vector DB :  
    #####################################################

    #벡터DB를 영구적으로 저장하여 재사용하기위해 저장 경로 미리 준비
    import os

    file_hash = get_file_hash(filename)
    root_path=f"./vector/"
    # base_dir = "../06_GenAI_project/vector_db"
    base_dir = f"{root_path}/vector_db"
    os.makedirs(base_dir, exist_ok=True)
    # db_path = f"../06_GenAI_project/vector_db/{file_hash}"
    # os.makedirs("../06_GenAI_project/vector_db", exist_ok=True)
    # db_path=f'./06_GenAI_project/chroma_vector_db_{filename}.db'  # chroma_vector_db_financial.db 는 폴더임. 
    db_path = os.path.join(base_dir, file_hash)


    if os.path.exists(db_path):
        #기존 벡터DB 로드 
        # pass
        vector_db=Chroma(persist_directory=db_path, embedding_function=embeddings)
        print('기존 벡터 DB 사용')
    else: #벡터 DB가 없는 경우
        #새로운 벡터 DB 만들기 -- 이때 임베딩 비용 지불  # 이때 돈들어감 
        # pass
        vector_db=Chroma.from_documents(chunks, embedding=embeddings, persist_directory=db_path)
        # 여기서 비용이 발생합니다.
        # 즉, 청크마다 임베딩을 생성하기 때문에 OpenAI API 사용료가 청구됩니다.
        # 현재 코드 구조에서는 같은 내용의 파일이라도 파일명이 다르면 다시 임베딩되어 비용이 발생할 수 있습니다.
        print('새로운 벡터 DB를 생성')
        st.write('새로운 벡터 DB를 생성')

        # 나중에 사용자가 질문하면
        # retriever.invoke("EMVA1288이란?") 또는 
        # vector_db.similarity_search("EMVA1288")
        # 를 호출할 것입니다. 이때도 비용이 발생할 수 있습니다.
        # 왜냐하면 질문도 임베딩해야 하기 때문입니다.



    print('저장된 벡터값 문서(청크) 개수',vector_db._collection.count())
    st.write('저장된 벡터값 문서(청크) 개수',vector_db._collection.count())


    
    #####################################################
    #### Set Vector DB as retriever :  
    #####################################################

    #RAG 파이프라인의 구성요소로 등록되도록 검색기 (리스티버)로 만들기
    retriever = vector_db.as_retriever(search_kwargs={'k':5}) #유사도상위 3개문서를 검색 kwargs: knowledge argument # 넌 이제 리트리버야.. 라고 해서 리트리버를 만듦. 
    #---------------------------------------------------


    #####################################################
    #### Set LLM(Brain) model :  
    #####################################################


    #WORK #2. [구성요소2] 두뇌(모델)
    from langchain_openai import ChatOpenAI
    model = ChatOpenAI( model='gpt-4o-mini',temperature=0.0,max_completion_tokens=10000,)


    #####################################################
    #### ChatPromptTemplate :  
    #####################################################

    #WORK #3. [구성 요소3] 지침 및 입력 
    from langchain_core.prompts import ChatPromptTemplate

    #프롬프트 엔지니어링 기법을 반영하여 탬플릿을 작성
    #단 알아둘것
    #RAG에서 사용자 질문과 맥락을 프롬프트에서 인식하기위해 정해놓은 변수명  - 책하고 다름 {context},{input}사용 : {input}이 과거에는 {question}이었다
    template = '''
    [역할 role]
    당신은 카메라업계에서 필요로 하는 카메라 개발과 평가에 대한 도움 챗봇입니다. 
    카메라와 관련한 개발과 평가와 관련된 도움을 주기 위해서 만들어졌어요.

    [목표 task]
    사용자의 질문에 대해 문맥으로 주어진 검색 결과를 바탕으로 답변해주세요.

    [문맥 context]
    {context}

    [제약조건 constraint]
    -검색결과에 없는 내용이면 답변할 수 없다고 해 주세요. 
    -반말,비속어등의 말은 하지 말아주세요.
    -초등학생도 이해할 수 있게 설명해 주세요.
    -영문이지만 한글로 만들어진 단어는 영어로 표현해 주세요. 만일 영어로 표현하기 힘들면 한글로 만들어 주세요.
    -설명을 위해 수식이 필요하면 수식을 사용해서 같이 설명해 주세요.

    [형식 format]
    -설명 후 주요개념을 5개 이내로 개조식으로 요약해 주세요.
    -각 주요개념은 bullet 기호를 사용해.

    질문:{input}
    답변:

    '''
    #현업에서는 위의 것보다 더 많은 프롬프트를 준다. 

    prompt = ChatPromptTemplate.from_template(template=template)
    #-------------------------------------------------------------
    

    #####################################################
    #### Memory Langchain :  
    #####################################################
    #일상 용어니 메모리는 건너띄자.



    #####################################################
    #### Make Langchains by using each objects [components] :  
    #####################################################

    #WORK #4. 위 3개의 구성요소를 모두 체인으로 연결 - 책은 retrieval-qa 인데 이거 이제 안됨.
    from langchain_classic.chains import create_retrieval_chain
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain  


    model_prompt_chain = create_stuff_documents_chain(llm=model, prompt=prompt) # LLM + ChatPromptTemplate
    rag_chain = create_retrieval_chain(retriever,model_prompt_chain)  # retriver + LLM + ChatPromptTemplate
    # #------------------------------체인을 다 묶어서 나의 체인을 만들었다. 여기까지-------------------------------------- 


    
    #####################################################
    #### Test implemented langchain :  
    #####################################################
    
    #WORK #5. [테스트]-- 테스트 완료 후 주서거리
    #사용자 질문을 프롬프트탬플릿으로 정의한 {'input':'질문'}형식으로 invoke() or stream()
    # response = rag_chain.invoke({'input':'너는 무슨 챗봇이야?'}) # 비용 발생
    # print(response) # 답변의 근거 문서부터 .. 토큰량 까지.. 모든 데이터들이 dict로 출력됨. 메타데이타 까지 다 나옴.
    # print('-'*30)
    # st.write(response)
    # st.markdown('---')

    #챗봇의 답변만 출력
    # print(response['answer'].strip()) #좌우 띄어쓰기 , 책에서는 answer 대신 result로 되어 있음.
    # print('~'*30)



    
    #####################################################
    #### UI configurat with Streamlit :  
    #####################################################
    # #WORK #6. [RAG AI 챗봇 UI제작 ] - gradio 모듈로 간단한 AI 금융챗봇 제작
    # import gradio as gr
    # with gr.Blocks() as demo : # 네모박스가 하나의 구성요소라고 보면 된다.
    #     # pass
    #     #마크 다운으로 제목 표시
    #     gr.Markdown('#금융용어가 어려우세요? 물어보세요') # #을 h1으로 인식
    #     #필요한 UI 구성요소 만들기 ( 채팅창, 입력박스 , 초기화버튼)
    #     chatbot = gr.Chatbot(label='MBCA AIX 경제금융용어 챗봇')
    #     input_box=gr.Textbox(label='질문해주세요')
    #     clear_button=gr.Button('대화초기화')


    # #[2] 아래 입력박스에서 제출버튼에 의해 실행될 함수 정의 
    # def get_response(input_question, chatbot_history): #등록된 요소의 내용물을 뽑아서 파라미터로 받음. 
    #     #위 WORK작업에서 만든 rag_chain에게 사용자 질문을 입력하고 응답받기(글씨만) , 근거도 받을 수 있으나 글씨만 받자
    #     response = rag_chain.invoke({'input':input_question})
    #     response_answer = response['answer'].strip()

    #     #챗봇 대화 내역에 질문과 답변을 추가
    #     chatbot_history.append({'role':'user','content':input_question})
    #     chatbot_history.append({'role':'assistant','content':response_answer})

    #     #다음 입력을 편하게 하기 위해 input_box요소에는 빈글씨를 , chatbot에게는 대화기록 리스트를 리턴해주기    return "",chatbot_history
    #     return "", chatbot_history
        

    # #[1] 사용자 입력을 제출하면 실행될 함수 등록 및 파라미터로 전달할 값을 가진 요소들 등록, 함수의 리턴값을 받을 요소들 등록
    # input_box.submit(get_response,[input_box,chatbot],[input_box,chatbot]) #gradio 에서 함수를 전달하면 그 값들이 요소로 빠져 나감... 즉 get_response의 파라미터들은 호출할때 함수명과 파라미터들에서 그 요소를 가져감. 




    # import streamlit as st

    # ----------------------------------------------------
    # 페이지 설정
    # ----------------------------------------------------
    st.set_page_config(
        page_title=f"{filename} 챗봇",
        page_icon="💰",
        layout="wide"  
    )

    # ----------------------------------------------------
    # 제목
    # ----------------------------------------------------
    name = os.path.splitext(filename)[0]
    # st.title(f"💰 {filename} 챗봇")
    st.markdown(f"## 💰 {name} 챗봇")
    # st.subheader(f"{filename}과 관련해서 궁금한 사항을 알려주세요.")
    st.subheader(f"{name}과 관련해서 궁금한 사항을 알려주세요.")

    st.markdown("---")



 
    # ----------------------------------------------------
    # 대화기록(Session)
    # ----------------------------------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []


    # --------------------------------------------
    # Session State 초기화
    # ---------------------------------------------
    # if "chat_history" not in st.session_state:
    #     st.session_state.chat_history = []





    # ----------------------------------------------------
    # 이전 대화 출력
    # ----------------------------------------------------
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # ---------------------------------------------
    # 이전 대화 출력
    # ---------------------------------------------
    # for message in st.session_state.chat_history:

    #     with st.chat_message(message["role"]):
    #         st.markdown(message["content"])





    # ----------------------------------------------------
    # 질문 입력
    # ----------------------------------------------------

    # ---------------------------------------------
    # RAG 응답 함수
    # ---------------------------------------------
    def get_response(input_question):

        # RAG 호출
        response = rag_chain.invoke(
            {
               "input": input_question
            }
        )

        response["answer"].strip()
        # response_answer = response["answer"].strip()

        # # 사용자 질문 저장
        # st.session_state.chat_history.append(
        #     {
        #         "role": "user",
        #         "content": input_question
        #     }
        # )

        # # 챗봇 답변 저장
        # st.session_state.chat_history.append(
        #     {
        #        "role": "assistant",
        #        "content": response_answer
        #     }
        #     )



    # ---------------------------------------------
    # 질문 입력
    # ---------------------------------------------
    question = st.chat_input("질문해주세요.")

    if question:

        # 사용자 질문 저장
        st.session_state.messages.append(
            {
                "role":"user",
                "content":question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)


        ####################################################
        # 여기에 RAG 호출
        ####################################################

        with st.spinner("답변 생성 중..."):

            response = rag_chain.invoke({"input":question})
            answer = response["answer"]

            # 테스트용
            # answer = f"질문하신 내용은 '{question}' 입니다."

        ####################################################

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":answer
            }
        )


    # #[3] '대화 초기화' 버튼을 누르면 모든 채팅 기록 삭제
    # clear_button.click(lambda:None, None, chatbot,queue=False) #gradio에서 명령들이 누적되어 늦게 실행되지 않도록 queue=False로 하면 즉각실행.
    # # None값을 lambda가 받으면 None을 받고 그것을 chatbot에 줘라..


    # ----------------------------------------------------
    # 대화 초기화 버튼
    # ----------------------------------------------------
    st.markdown("---")

    if st.button("🗑 대화 초기화"):

        st.session_state.messages = []

        st.rerun()



    # #Gradio 웹앱 실행
    # demo.launch(debug=True) # streamlit 처럼 터미널에 실행되는 url표시됨. https://127.0.0.1:7860번

    # #우리만의 RAG를 만든것이다. 
    # #회사는 자기만의 답을 받아야 한다.
    # #매뉴얼을 만들어 두고 그것을 이용해서 답을 얻으면 된다. 
    # #이것이 우리가 해야 할 업무이다. 


    ####################################################
    # Streamlit 배포
    ####################################################
        
    # RAG_Chatbot/
    # │
    # ├── main.py
    # ├── requirements.txt
    # ├── .env
    # ├── .gitignore
    # ├── README.md
    # │
    # ├── vector/
    # │   └── ...
    # │
    # ├── data/
    # │   ├── manual.pdf
    # │   └── sample.xlsx
    # │
    # └── images/    


    #Streamlit Community Cloud 배포 
    #1) 프로젝트를 GitHub에 업로드 
    
    #2) 그 다음에 Streamlit Cloud 접속 및 (GitHub계정)로그인 [ 회원가입했다는 전제]
    #   - 구글에서 검색 : streamlit community cloud
    #   - 사이트 우측 상단 Deploying? Try:Free | Pro 에서 Free로 login in with GitHub 를 클릭해서 로그인
    #   외부 모듈을 사용했다면 에러발생 .. streamlit cloud에는 module이 설치되어 있지 않기에...
    #   직접 설치는 안되고.. 특정 이름의 문서를 주면 이를 기반으로 자동 설치됨...
    #   파이썬의 모듈 목록을 저장해 놓은 문서 requirements.txt를 만들고 안에 설치할 모듈 목록 등록
    #   외부 api key를 사용한다면 역시 에러가 또 발생..
    #   .env 파일은 업로드 하면 완되는 비밀파일이기에..
    #   streamlit cloud에서 배포된 프로젝트마다 사용한 인증키나 비밀번호 같은 정보들을 
    #   설정해 놓을 수 있는 기능이 제공됨. 
        
    #3) [New app]버튼을 클릭 후 GitHub저장소를 선택 
    # 우측 상단 : create App -> deploy a public app from Github -> 

    #4) 그러면 자동으로 배포됨 (도메인 일부 수정 가능)







