# 메일의 inbox 등등을 가져오는 것  수신함... 
# 메일박스 수신함(Inbox)을 접근하는 외부모듈 설치
# pip install imap-tools 

# 설치 끝났으면 이제 시작

from account import *
from imap_tools import MailBox      # email access protocol 

#1. 메일박스를 읽어오기 위한 객체 생성
mailbox = MailBox('imap.gmail.com', 993) # imap 은 동기화가 좋음. IMAP port 번호 : 993 [Internet Mail Access Protocol]

#2. 로그인 , 특정 수신함을 열기 

mailbox.login(EMAIL_ADDRESS,EMAIL_PASSWORD,initial_folder='INBOX') # 플랫폼마다 달라서 확인하고 사용 , 수신함
#3, 메일함에서 최신순(reverse = True)으로 메세지를 읽어오기. 일단. 1개만...
for msg in mailbox.fetch(limit=1, reverse=True): # 기본이 False라서 옛날게 온다.
    print('제목:',msg.subject)
    print('발신자:',msg.from_) # 변수명에 _있음
    print('수신자:',msg.to) 
    print('참조:',msg.cc) # carbon copy : 먹지 
    print('비밀참조:',msg.bcc)
    print('수신날짜:',msg.date) # 시간대가 구글이어서 미국시간일 수 있음. # 서버는 미국 시간으로 되어 있고 한국 메일을 받으면 그것은 미국 시간을 한국 시간으로 바꿔 주는 것임.
    print('본문내용:',msg.text)
    print('HTML 메세지:',msg.html)
    print('-'*40)
    #혹시 첨부파일이 있다면 자동으로 다운로드 되도록...

    
    for file in msg.attachments:
        #원본파일메영 경로이름이 써있음. 분리
        path = file.filename.split('/')
        name=path[len(path)-1]
        # print('첨부파일명:', file.filename)
        print('첨부파일명:', name)
        print('첨부타입:',file.content_type)
        print('파일크기:',file.size, "bytes") # 몇 바이트 - 파일이 깨지면 0으로 나온다. 
        # with open('./{folder}')
        # with open('./04_email/rpa_mail_download_'+file.filename,'wb') as f:
        with open('./04_email/rpa_mail_download_'+name,'wb') as f:
            f.write(file.payload) # react 수업 때 함. 
            # print('첨부파일{} 다운로드 완료'.format(file.filename))
            print('첨부파일{} 다운로드 완료'.format(name))
        print('~'*30)

    #4. 메일반스에서 로그아웃
    #  이전에는 with를 했기 때문에 close가 자동으로 되는데 여기서는 하지 않아서 close 해야 함.

    mailbox.logout()