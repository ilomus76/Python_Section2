# 이것은 pyautogui가 있어야 하는 것이 아님. 원래 있는것이다.
#특정 프로그램을 자동 실행한느 방법


#0 파이썬의 표준라이브러리  : 즉 별도 설치안해도 있는것

import subprocess

#1. 크롬 브라우저 실행
# chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe" #경로   , 역슬래쉬를 해야 한다. 혹은 아래와 같이 r를 앞에 넣음.
chrome_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"


subprocess.Popen(chrome_path)

# 크롬 앱이 샐행 되길 잠시 대기
import time
time.sleep(1)

import pyautogui
pyautogui.hotkey('ctrl','t') #새탭열기
time.sleep(2)

#2. 메모장 앱 실행 -- 메모장 프로그램 설치 위치..알고 싶다면.. cmd창에 where notepad
notepad_path=r"C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\notepad.exe"
# notepad_path="C:\\Users\Admin\\AppData\Local\\Microsoft\\WindowsApps\\notepad.exe"
subprocess.Popen(notepad_path)

time.sleep(1)
pyautogui.write('Hello. nice to meet you ', interval=0.1)

#3. 단출기로 그림판 실행해 보기
pyautogui.hotkey('win','r') #검색 기능
pyautogui.write('mspaint') # 그림판 프로그램 명
pyautogui.press('enter')
