# 알림창을 띄우는 기능
import pyautogui

# 카운트 다운기능
pyautogui.countdown(3) #터미널차에 3,2,1..이 표시됨


#1. 간단한 디이얼로그
pyautogui.alert('This is alert dialog','경고') # 메세지, 제목

#동작도미. 
#2. 사용자 선택 다이얼로그 [확인]/[취소] : JS에도 있음.
answer = pyautogui.confirm('화일 탐색기를 여시겠습니까?','선택')
print(answer)

#3.사용자 입력 다이얼로그
age = pyautogui.prompt('나이를 입력하세요','나이입력')
print(age)


#3.1 비밀번호 입력 다이얼로그
pw = pyautogui.password('암호를 입력하세요')
print(pw)
#----------------------------------------------------------------

#4. 파일 탐색기(explorer)를 실행하기 [ 단축키 : winow키 + e]
pyautogui.hotkey('win','e')

import time
time.sleep(1) #탐색기 열릴때까지 잠시 대기

#특정 폴더로 이동 -- 주소창을 클릭하거나.. 단축키로 주소 입력 alt +d 하면 폴더의 주소창으로 이동
pyautogui.hotkey('alt','d')

# 역슬래쉬 , 슬래쉬로 하려면 // 로 해야 함
# cmd 창을 열어 그 안에서 where Document와 같이 찾거나 폴더의 오른쪽 클릭을 해서 "경로로 복사"로 카피해라
pyautogui.write('C:/Users/Public/Documents') # 항상 이 폴더가 있을 듯.
pyautogui.press('enter')
time.sleep(2)

#[수행과제] '문서' 폴더 안에 특정 파일형식의 파일을 찾아서 클릭하여 실행되도록.. [locateAllonScreen()기능 필요] --> 아이콘을 찾아서 실행.

 