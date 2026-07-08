# 인터넷 키고 구글 로그인
# Naver나 구글이나 형식은 똑같다. 
# 계정관리 -> 보안 및 로그인 -> 2단계 인증 사용 설정일 되어 있도록 해라.

# 이메일 전송 자동화 - google gmail 로 실습
# 이메일 전송하려면 로그인이 필요함. 단. 앱에서 로그인하는 [ 앱 비밀번호]를 이용 ~ 보안수준이 낮은 16자리 비밀번호
# 구글 로그인때 사용하는 것이 아니라 앱 비번이 따로 있다.

# 구글 계정 로그인 후 설정 필요
# [계정관리] 버튼을 누르면 ... 페이지의 좌측에 [보안 및 로그인] 메뉴 선택 ~ 2단계 인증이 되어 있어야 함. 
# 상단검색창에 '앱 비밀번호' 를 검색하면 앱 비밀번호 생성 페이지가 열림. 
# 이 앱만의 고유한 번호를 발급받기 ~ 16자리 글씨들.. 



# 이메일 주소와 앱비밀번호를 변도의 account.py 파일에 변수로 저장하고 import하여 사용 권장 
# import account
# from acount import *

from account import EMAIL_ADDRESS, EMAIL_PASSWORD
print(EMAIL_ADDRESS, EMAIL_PASSWORD) # 이렇게 하면 나중에 accout.py를 안올리면 정보를 모름. 

# 여기까지가 준비 끝

# 시작 .. 
# 이메일 전송을 위한 규약 : smtp [ simple mail transfer protocol]
# 이 규약을 이용하여 이메일을 전송해주는 파이썬의 표준모듈 : 즉 별도의 설치가 필요없음 . smtplib

import smtplib 

#SMTP 객체를 생성하여 메일 전송작업 수행 : 단 생성할 때 (메일서버명, 포트번호)
# with smtplib.SMTP('smtp.gmail.com',25) as smtp:   # smtp.naver.com , http가 아니고 smtp , 
# with smtplib.SMTP('smtp.gmail.com',465) as smtp:   #보안 업그레이드 
with smtplib.SMTP('smtp.gmail.com',587) as smtp:   # smtp.naver.com , http가 아니고 smtp , 
    smtp.ehlo() # 연결이 잘 되었는지 확인 [ extended Hello]
    smtp.starttls() # 모든 내용은 암호화 해서 전송해 달라는 설정. - tls [ transport layer security]
    # 위 두개 기본 

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD) # 이때 로그인이 됨. 

    #메일의 제목 , 내용
    subject = "TEST RPA EMAIL" #한글 안됨. 
    body = "this is rpa test mail" # 메일 본문

    #이메일을 보내는 정해진 형식 "Subject: 제목\n내용"
    message = f"Subject: {subject}\n{body}"  # f -string 
    smtp.sendmail(EMAIL_ADDRESS,"ilomus76@gmail.com",message) # 발신자 메일, 수신자 메일, 메세지(제목, 내용)
