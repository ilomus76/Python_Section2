#TTS : 텍스트를 자연스러운 음서응로 변환 TEXT to SPEECH

#구글 검색 해봐라 : openai tts api  
#https://developers.openai.com/api/docs/guides/text-to-speech

# openai에서 제공하는 tts 모델의 price
#1. gpt-4o-mini-tts [ 텍스트 입력 : 100만토큰 당 $0.60달러, 오디오출력 : 100만 토큰당 $1.2]
#2. tts-1 : 백만토큰당 $15.0
#3. tts-1-hd : 백만토큰당 $30.0 

#1. .env 에 있는 api key값 읽어오기
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI() # 키는 않읽어와도 됨 위에서 load_dotenv()가 읽어오기 때문

#음성으로 변환한 음성파일을 저장할 경로와 파일명 미리 지정
from pathlib import Path
audio_file_path= Path(__file__).parent / 'speech.mp3' # __file__ 현재파일이름의 경로가 출력 , 현재 실행 중인 파일이 위치한 폴더에 "speech.mp3"파일명으로 경로 만들기 
#pathlib 를 쓰면 모듈에서 / 연산자는 나눗셈이 아니라 경로를 결하(join)하는 연산자..
#macos, linux , windows 마다 경로구분자가 다른데.. 이를 알아서 해줌.

with client.audio.speech.with_streaming_response.create(
    model='gpt-4o-mini-tts' , # 제일 쌈
    voice='ballad',  # https://www.openai.fm/ 에서 목소리를 들어볼 수 있음
    input= '안녕하세요. 저는 AI 비서입니다.',
    instructions='밝고 친절한 톤으로 말해',
) as response:
    #응답결과에 바이트로 온다는것.
    response.stream_to_file(audio_file_path)