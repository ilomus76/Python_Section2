#첨부파일과 함께 메일 전송
# 회사업무 보고서 에 도움.


from account import * 
import smtplib
from email.message import EmailMessage

# 1. 이메일 객체 생성
msg = EmailMessage()

#2. 제목/ 발신자 / 수신자 / 본문내용
msg['Subject']='첨부파일 테스트 메일입니다.'
msg['From']=EMAIL_ADDRESS
# msg['To'] = 'ilomus76@naver.com'
msg['To'] = 'ilomus76@gmail.com'
msg.set_content('첨부파일을 보냅니다. 확인부탁드립니다.')

#3. 첨부파일 전송위해 파일을 binary mode 로 읽어와야 함. 파일은 글씨덩어리가 아니어서 이진수로 가져옴.
# 파일 타입(mime : multi purpurse mail extention) 을 전송할때 명시해야함. 
with open('./04_email/aaa.png','rb') as file:
    msg.add_attachment(file.read(),maintype='image',subtype='png',filename=file.name) # 파일 데이터 bytes, MIME type( main , sub) , 파일명(실제파일명을 안적어도 됨)  : text/html image/png first/sub 
    #마임타입을 알고 싶다면..   구글에 한번 검색 해 봐라. 
    # mime type list , https://developer.mozilla.org/ko/docs/Web/HTTP/Guides/MIME_types/Common_types

with open('./04_email/aaa.pdf','rb') as file:
    msg.add_attachment(file.read(), maintype='application',subtype = 'pdf',filename = file.name)

with open('./04_email/aaa.xlsx','rb') as file:
    # msg.add_attachment(file.read(),maintype='application' subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=file.name)  
    # subtype : 참조 사이트 https://developer.mozilla.org/ko/docs/Web/HTTP/Guides/MIME_types/Common_types

    # or 잘 모르겠으면 아래와 같이.. 가급적이면 위의 내용으로 ...
    msg.add_attachment(file.read(), maintype='application', subtype='octet-stream',filename = file.name)


#4. SMTP객체를 생성하여 이메일 메세지 전송
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()   # 전송계층에서 암호화가 됨 application layer가 아님. 
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)  

    smtp.send_message(msg)
