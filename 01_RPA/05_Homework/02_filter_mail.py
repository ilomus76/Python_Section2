# [선정 안내 메일] 
# 제목 : [선정] 모의 면접 신청 
# 본문 : OOO님 축하드립니다. 모의면접 대상자로 선정되셨습니다. ( 선정순번 1번 )  
# [탈락 안내 메일] 
# 제목 : [탈락] 모의 면접 신청 
# 본문 : OOO님 모의 면접 대상자에 아쉽게도 선정되지 못했습니다.  
# 취소 인원이 발생하는 경우 연락드리겠습니다. ( 대기순번 3번 )  


#   02_filter_mail.py]

#특정 조건의 메일만 필터링하여 읽기
from imap_tools import MailBox
from account import *

# with와 함께 하면 logout() 알아서 해줌
# with MailBox('imap.gmail.com',993) as mailbox: # 서버 , 포트번호
#     pass

content = []


#위의 것을 포함해서 로그인 까지 한번에
with MailBox('imap.gmail.com',993).login(EMAIL_ADDRESS,EMAIL_PASSWORD,initial_folder='INBOX') as mailbox: # 서버 , 포트번호
    # pass
    
    count = 0
    for msg in mailbox.fetch(limit=10,reverse=True):
        if "면접" in msg.subject:            
            print(f'보낸사람: {msg.from_}-제목:{msg.subject}- 내용:{msg.text} -시간:{msg.date}')
            count +=1
            content[count]['보낸사람']=msg.from_ 
            content[count]['보낸사람']=msg.from_
            

        