# [open ai 토큰계산기 ] : https://platform.openai.com/tokenizer


from google import genai





def get_president_korea():
    """
        # doc string :
        이 함수는 대한민국 대통령에 대한 질문을 답변하기 위해 사용됩니다.
    """

    return "이재명"

def get_weather():
    #기상청 open api 를 통해 날씨 데이터를 가져오기
    import requests
    weather = requests.get('기상청 open api.json') ## 실제 open api 작업할것이
    return weather




from google.genai import types
config=types.GenerateContentConfig(
    max_output_tokens=500, 
    temperature=2.0,  
    top_p=0.5,
    # top_k=20,
    # response_mime_type='text/plain',   
    # response_mime_type='application/json',   
    # seed=42,
    # system_instruction='너는 고양이야 이름은 네코에코야', #프럼프트 엔지니어링  
    # system_instruction='너는 불량한 고등학생이야. 답변도 비속어를 섞어서 해',
    system_instruction='당신은 이미지센서 전문가입니다. 자동차 분야의 이미지 센서 시장의 기술 트렌드에 기반해서 알려주세요.',

    # tools=[함수명1, 함수명2]
    # tools=[get_president_korea],     
    # tools=[get_president_korea,get_weather],  
  

)


client = genai.Client(api_key='GOOGLE_API_KEY')  #https://aistudio.google.com/api-keys



response = client.models.generate_content( # 텍스트를 생성해주는 함수 , 응답이 옴
    model='gemini-3.5-flash', 
    contents= "2026년 자동차 이미지 센서 업계 동향은?",
    config= config,
)

# print(response)
print(response.text)