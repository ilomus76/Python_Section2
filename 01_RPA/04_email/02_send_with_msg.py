from account import EMAIL_ADDRESS,EMAIL_PASSWORD
import smtplib
#한글과 첨부파일등의 함께 보낼  수 있는 EmailMesssage 클래스 사용

from email.message import EmailMessage  # 이것이 이메일의 형식을 자동으로 만들어 줌.

# 1. 이메일 객체 생성
msg = EmailMessage()

# 제목 / 발신자 주소/   수신자 주소를 설정

msg['Subject'] = '테스트 메일입니다' # 제목
msg['From'] = EMAIL_ADDRESS # 발신자 메일주소
#msg['To'] = 'ilomus76#gmail.com' #수신자 메일주소   : 1명에게 보내기

#5 여러명에게 전송하는 메일이라면..   
mail_list = [ 'ilomus76@gmail.com', 'ilomus76@naver.com' , 'ydg57013@gmail.com']
msg['To'] =",".join(mail_list) # 파이썬의 리스트를 특정 문자기준으로 합친 문자열 

#6. 참조
msg['Cc'] = 'ilomus76@naver.com' # Carbon Copy
#비밀참조
# msg['Bcc'] = 'ilomus76@gmail.com' #blined CC
msg['Bcc'] = 'ilomus76@naver.com' #blined CC


#3. 메일의 본문내용 
msg.set_content('이 메일은 테스트 메일입니다. 자동화된 메일 시스템을 구축할 수 있어요\n 한글도 잘 보내집니다.') # 줄바꿈

#4. SMTP 객체를 생성하여 메일 메시지 전송
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)
