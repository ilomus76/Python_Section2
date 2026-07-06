#엑셀 사용을 위한 외부 모듈 설치 openpyxl 오픈파이엑셀

# 0 . pip install openpyxl

#1. 엑셀파일 객체를 Workbook 클래스를 통해 만들 수 있음.  : book.xlxs 로 되는 이유.. 
from openpyxl import Workbook # 말하는 것처럼 써라.

#2. 워크북 객체 생성
wb = Workbook()  # 객체 생성


#3. 워크북에서 sheet를 여러개 만들 수 있음. 워크북 안에 현재 활성화 된 워크시트 참조(default sheet 이름 'Sheet1')
sheet=wb.active

#4. 워크북 객체를 엑셀 파일로 저장
# wb.save('./sample.xlsx')  # 01_RPA 가 폴더가 됨. 
wb.save('./01_excel/sample.xlsx')  # 01_RPA 가 폴더가 됨. 

#5.워크북 닫기
wb.close()

# 프로그램으로 실행해서 만든것이다. RPA
