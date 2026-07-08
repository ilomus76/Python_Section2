# [신청 메일 양식] 
# 제목 : 모의 면접 신청합니다. 
# 본문 : 과정명 / 이름 / 전화번호 뒤 4자리   (예) aix / 홍길동 / 1234 
# [ # 실행 결과를 테스트 하기 위해 6명의 신청 메일을 자동으로 전송하는 자동화코드 작성  01_send_apply_mail.py]


from account import EMAIL_ADDRESS,EMAIL_PASSWORD
import smtplib
#한글과 첨부파일등의 함께 보낼  수 있는 EmailMesssage 클래스 사용

from email.message import EmailMessage  # 이것이 이메일의 형식을 자동으로 만들어 줌.

# 1. 이메일 객체 생성
msg = EmailMessage()

# 제목 / 발신자 주소/   수신자 주소를 설정


subject = '모의 면접 신청합니다.'
content = [

    {'과정명':'aix','이름':'손흥민','전화번호뒤4자리':'1234','email':'ilomus76@gmail.com'},
    {'과정명':'web','이름':'김민재','전화번호뒤4자리':'5678','email':'ilomus76@gmail.com'},
    {'과정명':'aix','이름':'류현진','전화번호뒤4자리':'1111','email':'ilomus76@gmail.com'},
    {'과정명':'aix','이름':'박찬호','전화번호뒤4자리':'2222','email':'ilomus76@gmail.com'},
    {'과정명':'web','이름':'김연아','전화번호뒤4자리':'3333','email':'ilomus76@gmail.com'},
    {'과정명':'design','이름':'박세리','전화번호뒤4자리':'4444','email':'ilomus76@gmail.com'}
]


# msg['Subject'] = subject # 제목
# msg['From'] = EMAIL_ADDRESS # 발신자 메일주소
# #msg['To'] = 'ilomus76#gmail.com' #수신자 메일주소   : 1명에게 보내기

# #5 여러명에게 전송하는 메일이라면..   
# mail_list = [ 'ilomus76@gmail.com', 'ilomus76@naver.com' , 'ydg57013@gmail.com']
# msg['To'] =",".join(mail_list) # 파이썬의 리스트를 특정 문자기준으로 합친 문자열 

# #6. 참조
# msg['Cc'] = 'ilomus76@naver.com' # Carbon Copy
# #비밀참조
# # msg['Bcc'] = 'ilomus76@gmail.com' #blined CC
# msg['Bcc'] = 'ilomus76@naver.com' #blined CC


# #3. 메일의 본문내용 
# msg.set_content('이 메일은 테스트 메일입니다. 자동화된 메일 시스템을 구축할 수 있어요\n 한글도 잘 보내집니다.') # 줄바꿈

#4. SMTP 객체를 생성하여 메일 메시지 전송

for count in range(0,len(content)):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        msg = EmailMessage()

        msg['Subject']=subject
        msg['From']=content[count]['email']
        msg['To'] = 'ilomus76@gmail.com'
        msg.set_content(content[count]['과정명']+'/'+content[count]['이름']+'/'+content[count]['전화번호뒤4자리'])
        smtp.send_message(msg)
