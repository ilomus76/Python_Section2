#특정 조건의 메일만 필터링하여 읽기
from imap_tools import MailBox
from account import *

# with와 함께 하면 logout() 알아서 해줌
# with MailBox('imap.gmail.com',993) as mailbox: # 서버 , 포트번호
#     pass

#위의 것을 포함해서 로그인 까지 한번에
with MailBox('imap.gmail.com',993).login(EMAIL_ADDRESS,EMAIL_PASSWORD,initial_folder='INBOX') as mailbox: # 서버 , 포트번호
    # pass

    #전체 메일 가져오기(메일이 너무 많으면 읽어올때 시간이 오래 걸림. limit=20로 제한해라)

    # 실행 1 - 주석하면서 내려가자
    # for msg in mailbox.fetch(limit=20): # 너무 많으면 20로 제한해서 테스트 해라.
    #     print(f'보낸사람: {msg.from_}-제목:{msg.subject}')


    # 실행 2
    #읽지 않은 메일만 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'): # 정해진 글자 (UNSEEN)
    # for msg in mailbox.fetch('(UNSEEN)',limit=10): # 정해진 글자 (UNSEEN) - 너무 많으면 limit을 넣어라. 
    #     print(f'보낸사람: {msg.from_}-제목:{msg.subject}')

   # 실행 3
    #특정인이 보낸 메일만 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'): # 정해진 글자 (UNSEEN)
    # for msg in mailbox.fetch('(FROM ilomus76@naver.com)',limit=10): # 정해진 글자 (FROM) - 발신자 
    #     print(f'보낸사람: {msg.from_}-제목:{msg.subject}')

    
   # 실행 4
    #(제목,본문)에 특정 문자열이 포함된 메일만 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'): # 정해진 글자 (UNSEEN)
    # for msg in mailbox.fetch('(TEXT "test mail")',limit=10): # 정해진 글자 (TEXT "문자열") <-- 반드시 큰따옴표
    #     print(f'보낸사람: {msg.from_}-제목:{msg.subject}')

    
  # 실행 5
    #제목에만 특정 문자열이 포함된 메일만 가져오기 --한글은 안됨. 영어만 찾아짐. 
    # for msg in mailbox.fetch('(UNSEEN)'): # 정해진 글자 (UNSEEN)
    # for msg in mailbox.fetch('(SUBJECT "test mail")',limit=10,reverse=True): # 정해진 글자 (SUBJECT "문자열") <-- 반드시 큰따옴표
    #     print(f'보낸사람: {msg.from_}-제목:{msg.subject}')

    
  # 실행 6
    #한글로 검색되게 하려면.. 전체메일을 가져온후 반복문으로 코드를 구현

    # for msg in mailbox.fetch(limit=10,reverse=True):
    #     if "테스트" in msg.subject:
    #         print(f'보낸사람: {msg.from_}-제목:{msg.subject}')

   # 실행 7
    # 특정 날짜 이후에 수신된 메일만 가져오기
    # for msg in mailbox.fetch('(SENTSINCE 01-Jul-2026)',limit=10,reverse=True): # 미국 시간 규약 기진 , 2026년 7월 8일 이후 
    #     print(f'보낸사람: {msg.from_}-제목:{msg.subject}')

   # 실행 8
    # 특정 날짜에 수신된 메일만 가져오기
    # for msg in mailbox.fetch('(ON 08-Jul-2026)',limit=10,reverse=True): # 미국 시간 규약 기진 , 2026년 7월 8일 이후 
    #     print(f'보낸사람: {msg.from_}-제목:{msg.subject}')

   # 실행 9
    # 2개 이상의 조건을 사용해야 할때 열겨하면 됨
    # 특정 날짜에 특정인으로 부터 수신된 메일만 가져오기
    # for msg in mailbox.fetch('(ON 08-Jul-2026 FROM ilomus76@naver.com)',limit=10,reverse=True): # 미국 시간 규약 기진 , 2026년 7월 8일 이후 
    #     print(f'보낸사람: {msg.from_}-제목:{msg.subject}')

   # 실행 10
    # 2개 중 하나이상의 조건을 만족할때 . OR...
    # 특정 날짜에 특정인으로 부터 수신된 메일만 가져오기
    # for msg in mailbox.fetch('(OR ON 08-Jul-2026 FROM ilomus76@naver.com)',limit=10,reverse=True): # 미국 시간 규약 기진 , 2026년 7월 8일 이후 
    #     print(f'보낸사람: {msg.from_}-제목:{msg.subject}')

  # time 모듈을 이용하여 특정 날짜의 미국 약어 표시 만들 수 있음.
    import time
    print(time.strftime('%d-%b=%Y')) #%b - month 의 약어 표기(Abbreviated : 약어)
    print(time.strftime('%a')) #%a -요일 약어
 


