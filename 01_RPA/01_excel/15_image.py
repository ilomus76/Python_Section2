from openpyxl import Workbook
wb= Workbook()
sheet = wb.active

# 엑셀 파일에 이미지를 그리려면.. jpg를 파이썬에서 다룰 수 있는 이미지로드 외부모듈 필요-- pillow (1부에서 설치함. 하지만 가상환경에서 설치안함. pip install pillow)
from openpyxl.drawing.image import Image

img = Image('./01_excel/paris.jpg')

sheet.add_image(img,'C3')



img.width=100
img.height=100 
# 사이즈 지정 안하면 원본 사이즈가 됨

#엑셀 기본 눈금선 안보이도록
sheet.sheet_view.showGridLines=False

wb.save('./01_excel/sample7.xlsx')
wb.close()