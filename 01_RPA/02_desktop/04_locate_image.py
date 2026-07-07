#화면에서 특정 이미지에 해당하는 위치(좌표)를 찾아서 제어하기 ~자동화에 많이 사용

# -- 해상도나 색상에 따라 검출이 잘 안될 수 있음. 
#배율을 100% 아니면 검출 잘 안됨. 
# 주모니터에세만 대상을 검색함.

import pyautogui

#1. 특정 이미지에 해당하는 그리믕ㄹ 화면에서 찾기
menu = pyautogui.locateOnScreen('./02_desktop/menu.png')    # pyautogui에게 위치를 찾아줘 스크린 위에서
print(menu) #Box(left=00, top=00, width=00, height=00)  , 못찾으면 에러.. 실무에서는 예외처리


#2.찾은 영영ㄱ을 클릭하기
pyautogui.click(menu) #Box 여역의 가운데를 클릭!


#3. 같은 이미지가 여러개 있을 경우 [ locateOnScreen()--> locateAllOnScreen()]
# w3schools checkbox 사이트    : https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox
checkboxs = pyautogui.locateAllOnScreen('./02_desktop/checkbox.png')    # pyautogui에게 위치를 찾아줘 스크린 위에서
print(checkboxs)
# 이 경우 해당 사이트를 오른쪽에 놓고 이 프로그램을 돌려야 수행이 됨


# #개수만큼 반복하며 클릭하여 체크하기
for checkbox in checkboxs:
    pyautogui.click(checkbox,duration=0.5)



# # 강사님은 성공 나는 동작 안함.

