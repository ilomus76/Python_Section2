# 알림창을 띄우는 기능
import pyautogui

#4. 파일 탐색기(explorer)를 실행하기 [ 단축키 : winow키 + e]
pyautogui.hotkey('win','e')

import time
time.sleep(1) #탐색기 열릴때까지 잠시 대기

#특정 폴더로 이동 -- 주소창을 클릭하거나.. 단축키로 주소 입력 alt +d 하면 폴더의 주소창으로 이동
pyautogui.hotkey('alt','d')


# target_folder_path= r"C:\Users\Admin\Documents"
# pyautogui.write(target_folder_path)  # r : raw 
# pyautogui.write(r"C:\Users\Admin\Documents") 
pyautogui.write(r"C:\Users\Public\Documents") 
# 폴더의 경로에 \ 가 있는 경우 특수문자표현에 제약이 있으니 /로 바꾸거나 \\을 사용하거나 'r'을 문자열 앞에 붙여 사용하라.
pyautogui.press('enter')
time.sleep(2)

# pyautogui.press('f11')
# pyautogui.press('enter')
# time.sleep(2)

# pyautogui.hotkey('alt', 'space')
# time.sleep(0.5)
# pyautogui.press('x')   # 최대화(Maximize)


# import glob

# files = glob.glob(target_folder_path+"\*.csv")

# for file in files:
#     print('filename : ',file , '\n','identified files number : ',len(files) )

# target_extensions = pyautogui.locateAllOnScreen('./02_desktop/ico1.png')
# print(target_extensions)

# for target_extension in target_extensions:
#     pyautogui.click(target_extension,duration=0.5)


try:
    target_extensions = list(
        pyautogui.locateAllOnScreen("./02_desktop/ico1.png")
    )

    if len(target_extensions) == 0:
        print("이미지를 찾지 못했습니다.")
    else:
        for target in target_extensions:
            print(target)
            pyautogui.click(target)

except pyautogui.ImageNotFoundException:
    print("이미지를 찾지 못했습니다.")





