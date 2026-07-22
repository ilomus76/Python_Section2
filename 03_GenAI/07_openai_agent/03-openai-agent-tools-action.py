#agent가 실제 동작을 수행하도록..

#(실습1) 메모장 작성
from agents import function_tool
@function_tool
def open_notepad(response:str):
    ''' Windows 메모장을 실행하고 사용자의 질문에 대한 답변을 파라미터 response로 받습니다.'''

    #메모장에 써질 글씨 확인
    print('AI 응답:',response)
    #1) 메모장 앱 실행 
    import subprocess
    subprocess.Popen(r'C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\notepad.exe') # Processor를 열어줘 실행해줘..
    # cmd 창에서 
    # C:\Users\Admin>where notepad
    # C:\Windows\System32\notepad.exe
    # C:\Windows\notepad.exe
    # C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\notepad.exe   <- 이것이 퍼미션이 따로 없어 사용.

    #### RPA 수업 때 한것임 #######################################
    #2) 메모장 앱이 실행되길 잠시 대기 한 후 글 작성 
    import time
    time.sleep(2) # RPA 수업때 한것임. 

    #3)글쓰기 - 한글은 안써짐.. 할글도 되려면.. 억지로 기능을 만들어야 함.
    #pip install pyperclip
    import pyperclip 
    #pip install pyautogui
    import pyautogui
    def slow_type_hangul(text, interval=0.25):
        for char in text:
            pyperclip.copy(char)        #한 글자씩 복사
            pyautogui.hotkey('ctrl','v') #붙여넣기
            time.sleep(interval)
    slow_type_hangul(response,interval=0.01)
    #---------------------------------------------------

    return "메모장을 실행했습니다."
#----------------------------------------------------------------------------

#(실습2)웹 브라우저 열기
@function_tool
# def open_webbrowser(url:str, params:str): # 파라미터 때문에 

# ''' 웹브라우저를 엽니다. 전달받은 url 웹페이지를 열고 params로 받은 정보를 바탕으로 웹 검색 작업을 수행합니다.'''
def open_webbrowser(url:str):
    ''' 웹브라우저를 엽니다. 전달받은 url 웹페이지를 열고 질문 정보를 바탕으로 웹 검색 작업을 수행합니다.'''
    import webbrowser
    webbrowser.open(url=url)  # url에 검색어가 딸려 있을것이다.
    return "웹 브라우저를 열었습니다."



# agent 만들기 
from dotenv import load_dotenv
load_dotenv()

from agents import Agent,Runner
agent = Agent(
    #모델 안써도 되고 그러면 가장 최신것으로 함.
    name='RPA Agent',
    model='gpt-4o-mini',
    instructions='''
    너는 사용자의 질문을 간결하게 대답하며 사용자의 요청을 수행하는 에이전트야.
    open_notepad 함수를 사용한다면(할지 안할지 우리는 모르니까) 질문의 답변은 open_notepad함수의 파라미터 response에 전달해줘.
    open_webbrowser함수를 사용한다면 요청을 수행하기 위한 url을 함수의 파라미터로 전달해줘. 
    
    작업 수행내역을 간단하게 정리햐여 응답해줘.
    bullet poiont를 사용해.
    ''',
    tools=[open_notepad, open_webbrowser]   # 이것을 사용하는 판단은 자기가 알아서 할것이다. 
)
# 오전에는 함수를 스키마를 내가 만들었는데 여기서는 agent가 알아서 말로 듣고 그것을 실행해줌.

#(실습1)
#response = Runner.run_sync(agent,input='AI 개발자가 되기 위한 학습 방법을 간단하게 요약해서 메모장에 저장해줘.') # 이 질문을 채팅창에 쓰는 것임.
#AI에게 질문했더니 메모장을 열어줬다. 

# 사실 use computer도 생겼고 그것은 인증까지 해야 해서 우리가 알기 복잡하다. 




#(실습2)
response = Runner.run_sync(agent,input='이번 주말에 일본여행을 갈거야. 항공권 정보좀 보여줘') # 이것은 메모장을 만들 수 있는 것이 아님. 그래서 함수를 더 만들것임.
# response = Runner.run_sync(agent,input='오늘 송파구에서 저녁모임이 이썽. 맛집정보를 볼수 있도록 네이버 겸색결과 페이지를 열어') '


# agent를 이런 기능을 하나에 몰아서 주면 너무 성능이 않좋으니 이것을 분산시켜 활용하는데 이걸 openai가 잘 해 두었다. 
# handoff 기술로 가자.