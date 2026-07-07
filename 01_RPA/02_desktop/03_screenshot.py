import pyautogui # 파이썬을 이용한 오토 그래픽 유저 인터페이스

#1. 현재 화면을 스크린샷을 찍어서 이미지로 저장
img = pyautogui.screenshot()
img.save('./02_desktop/aaa.png') # workspace는 01_RPA가 기준임   - 화면이 찍힘. -듀얼 모니터는 안됨 . 주 모니터만 됨.

#2. 특정 범위를 캡처하기 
img2 = pyautogui.screenshot(region=(70,120,200,100)) #left, top, width ,height
img2.save('./02_desktop/bbb.png')


#3. 듀얼모니터를 사용한다면..
img3 = pyautogui.screenshot(allScreens=True)
img3.save('./02_desktop/ccc.png')



# 안됨. 