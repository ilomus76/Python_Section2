# streamlit 모듈을 이용하여 chatbot UI 구성 방법 실습 
# 드디어 국내 소버린 AI LLM이 무료로 나온다. 

# 0. 모듈
# pip install streamlit 
# 파이썬을 이용해서 
# 가상환경 안하기로 함. 

# 1. 모듈 사용 

import streamlit as st

#2. 채팅 메세지 UI 를 만드는 기능함수 
# 어제는 기본 웹사이트를 출력하는 기능만 했고..
# 오늘은 위에서 아래로 나오는데 아이콘 다르게 오른쪽 왼쪽에 

with st.chat_message('user'): # human 과 user가 동일했는데.. 4개중에 아무거나 써도 됨. user - assistant 가 지금은 human -ai로 대응
    st.write('안녕하세요.')

with st.chat_message('assistant'):
    st.write('반가워요~')

#'role'역할에 없는 명칭을 사용하면 첫글자 표시
with st.chat_message('bot'):
    st.write('this is bot')

with st.chat_message('sam'):
    st.write('this is sam')

with st.chat_message('홍길동'):
    st.write('나는 홍길동입니다.')
    st.write('반가워요')
    st.button('눌러주세요')

#한줄로 간결하게..
st.chat_message('ai').write('한줄로써도 됩니다.')  # ai와 assistant는 같은것임.
st.divider()

#3) 채팅처럼 대화하는 형태가 되려면 각각의 메세지들을 리스트로 잘 보관되어 있어야 함.
# 단, 메세지 데이터는 딕션너리로 만들어서 순서는 {역할:'', 내용:''} 구조(스키마)구조로 만들어야 함.
messages= [
    {'role':'assistant','content':'무엇을 도와드릴까요?'},
    {'role':'user','content':'대한민국의 수도는?'},
    {'role':'assistant','content':'대한민국의 수도는 **서울**입니다.'}, # 마크다운으로 strong tag ** xx **
    {'role':'user','content':'오. 고마워~~'},

] # 이런것을 보통 데이타베이스에 저장해서 가져올수 있음.

for msg in messages:

    with st.chat_message(msg['role']):
        st.markdown([msg['content']])
st.divider()

#3) 사용자 채팅메세지 입력 UI

# streamlit은 react로 그리기 때문에 화면을 다시 그림. 그래서 그전께 다 지워짐. 
# 이전 채팅메세지가 사라질것임. streamlit의 렌더링 방식때문에 .. 새로운 메세지가 입력될때마다 이 프로그램을 처음부터 다시 실행함.
# 즉 state화면갱신과 같음. 

# 그래서 화면이 갱신되어도 데이터를 저장하는 변수를 streamlit에서 제공함. 
#st.session_state 라고 부름 session은 연결. 프로그램이 진행중인... 이라는 뜻. 연결되어 있을때만 상태값을 저장한다는 뜻의 session임.

# a. message라는 이름의 변수가 st.session_state에 존재하는지 부터 확인하고 첫 문장 저장
if "messages" not in st.session_state:
    #"messages" 라는 키워드가 없으면 session_state에 messages라는 키워드를 넣어라... 
    # a = { 'name':'test'} 
    # a.message = 'sss' 로 하면 a 가 a = {'name':'test' , 'message':'sss'} 가 됨
    # a.message = 'sss' 와 a['message'] = 'sss'는 같은 뜻임. 
    st.session_state.messages=[
        {'role':'assistant','content':'무엇이든 물어보세요'},
    ]
#b. st.session_state 에 저장된 "message"리스트들을 채팅메세지로 그려내기
for msg in st.session_state.messages:
    st.chat_message(msg['role']).markdown(msg['content'])

question = st.chat_input('질문을 입력하세요') # 화면의 맨 아래쪽에 위치 - enter 입력완료. shitf-enter 줄바꿈
if question: # 질문이 들어왔다면
    question = question.replace('\n','  \n') # 띄어쓰기 2번 \n이 줄바꿈하는 markdown
    st.session_state.messages.append({'role':'user', 'content':question})
    st.chat_message('user').write(question)

    #입력 메세지에 대해 ai 모델을 이용하여 응답하도록.. 지금은 실습을 위해....Mock데이타 목업데이타
    response = f'{question}에 대해 알고 싶군요.  \n 어쩌고 저쩌고....' # 마크 다운에서 줄바꿈은 \n앞에 띄어쓰기 2개 # 나중에 여길 ai로 해야 함.
    st.session_state.messages.append({'role':'assistant', 'content':response})
    # st.chat_message('assistant').write()
    st.chat_message('assistant').markdown(response)

    



#------------------------------------------------------

#[실행] 스트림릿을 실행하면 명령어를 터미널에서 수행
#streamlit run 파일명.py