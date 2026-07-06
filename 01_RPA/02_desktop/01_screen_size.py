# 주모니터로 해야 함. 
# python의 desktop 자동화 외부 모듈 설치 : pyautogui [ pip install pyautogui] : 내경우 가상환경이 꺼져서 글로벌 환경에서 함. 
#1. import 
import pyautogui

#2. 현재 화면 ( 스크린- 모니터) 사이즈 알아보기
size = pyautogui.size()
print(size)
# Size(width=1920, height=1080)
print()

# --------- 듀얼 모니터..를 사용할때 모니터별 사이즈 알고 싶다면... 추가모듈 screeninfo [ powershell 에서 pip install screeninfo]
from screeninfo import get_monitors

#모든 모니터 정보 가져오기
monitors = get_monitors()

#0번이 주 모니터, 1번이 보조 모니터 
if len(monitors)>1:
    secondary = monitors[1] 
    print(f'보조 모니터 크기: {secondary.width} x {secondary.height}')
    print(f'보조 모니터의 위치(좌표): {secondary.x}, {secondary.y}')
else:
    print('보조 모니터가 감지되지 않았습니다.')

#result : 복제면 없다고 나옴
# 보조 모니터 크기: 1920 x 1080
# 보조 모니터의 위치(좌표): 0, -1080