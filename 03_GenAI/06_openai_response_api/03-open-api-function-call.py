#함수 호출 도구 사용이 워크플로(파이프라인)
#사용자 질문 - 1차. Response API 에게 질문을 할것이고.. -> 모델이 스스로 (일반적인 답변을 할지 or 함수를 콜할지 function_call 할지 선택)
#(만약. 함수호출이 필요하다고 선택했을 경우) : -> 파이프라인이 갈라진다. -> 내가 만든 함수 실행 -> 실행결과를 function_call_output 전송 -> 이걸 2차. response api가 받아야 함. ->최종 답변
# 함수가 필요해 하고 답변을 안하고 그 답변을 우리가 만들어야 함... 
# (만약. 함수호출이 필요없다면) : -> 1차 응답결과를 출력   
# 질문ㅇ르 LLM에게 주면 함수호출 필요있냐? 없으면 대답함 있으면 함수가 필요해라고 알려주고... 그 함수를 호출해서 그 결과를 다시 LLM에게 주고 그것을 바탕으로 2차 응답. 
# 옛날에 구글 , openai가 달랐는데 지금은 같아짐.

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

#1. 답변에 사용할 도구 설정 : 함수 호출. 도구로 사용할 함수의 구조를 미리 설계(모델에게 알려줄 함수의 명세서 JSON schema-딕셔너리로 생겼어라고 알려줌)
#{'type':'web_search'}, , 규격1
# {'type':'file_search','vector_store_ids':['vs_6a5d7ca88c64819183ee30953904b54d']}, 규격2

#규격3

# def get_weather(city)
tools = [
    {
        "type":"function",
        "name":"get_weather",
        "description":"현재 날씨를 조회한다.",
        "parameters":{
            "type":"object", #파라미터가 여러개일수 있어서.. 객체로... 여러개 속성을 가지고 있다는 것.. 마치 properties와 같음  # 즉 아래의 city와 같은 것이 여러개이기 때문에 object임.
            "properties":{
                "city":{
                    "type":"string",
                    "description":"도시 이름",
                    #코드없이 코드를 짜는 모습. 스키마를 짜는 모습이 이런 모습 , 노코드 베이스 프로그램. 스키마는 규격, 명세서라고  생각해라.

                }
            },
            "required":["city"],
        }
    }

 ]  


# 2. 사용자의 질문에 함수호출이 필요한지 모델이 판단하도록 1차 responses api 요청 
response = client.responses.create(
    model='gpt-4o-mini',
    #질문을 2종류로 나눠볼게요.
    # (1) 함수호출이 필요할만한 질문
    # input = '현재 서울 날씨 알려줘' , # 이것은 이미 학습된 llm이 답변할 것이다.
    #(2) 함수호출이 필요없는 질문
    input='서울은 어느나라의 수도인가?',
    #질문은 한번에 하나씩. input은 2개가 되지 않음

    tools= tools, #도구지정
    tool_choice='auto' # 모델이 알아서 도구 사용 여부를 결정 -- default

)
#응답결과 출력 
print(response) #텍스트아님  , 원래 response output만 하면 되는데...
#만약, 모델이 함수를 호출해야 한다고 판단하면 JSON 구조로 응답함.    
print()
print(response.output)   # print(response.output_text)하면 아무것도 안나올거라고 함. 이것은 function call이 json code화 되어 있기 때문인듯. 
print()


# 현재 서울 날씨 알려줘 의 질문을 가지고 서울이 도시인지도 모르는데 알아서 자기가 파라미터로 전달 arguments.  -> 아래의 output=[ResponseFunctionToolCall(arguments='{"city":"서울"}', call_id='call_qSL0aTfrVmEZm6DtxS5RK8I9', name='get_weather', type='function_call', 을 보면 type의 function call이 되어 있기에 함수를 실행하고 파라미터를 던짐.
# PS C:\Users\Admin\MBCA\Python2\03_GenAI> & C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe c:/Users/Admin/MBCA/Python2/03_GenAI/06_openai_response_api/03-open-api-function-call.py
# Response(id='resp_03395d7371718a9e006a5d8546988c81988cbd97112ce7a68c', created_at=1784513863.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='gpt-4o-mini-2024-07-18', object='response', output=[ResponseFunctionToolCall(arguments='{"city":"서울"}', call_id='call_qSL0aTfrVmEZm6DtxS5RK8I9', name='get_weather', type='function_call', id='fc_03395d7371718a9e006a5d854a6d5081988c22efb6ffa0b465', caller=None, namespace=None, status='completed')], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[FunctionTool(name='get_weather', parameters={'type': 'object', 'properties': {'city': {'type': 'string', 'description': '도시 이름'}}, 'required': ['city'], 'additionalProperties': False}, strict=True, type='function', allowed_callers=None, defer_loading=None, description='현재 날씨를 조회한다.', output_schema=None)], top_p=1.0, background=False, completed_at=1784513866.0, conversation=None, max_output_tokens=None, max_tool_calls=None, moderation=None, previous_response_id=None, prompt=None, prompt_cache_key=None, prompt_cache_options=None, prompt_cache_retention='in_memory', reasoning=Reasoning(context=None, effort=None, generate_summary=None, mode=None, summary=None), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=48, input_tokens_details=InputTokensDetails(cache_write_tokens=0, cached_tokens=0), output_tokens=15, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=63), user=None, billing={'payer': 'developer'}, frequency_penalty=0.0, presence_penalty=0.0, store=True, tool_usage={'image_gen': {'input_tokens': 0, 'input_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'output_tokens': 0, 'output_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'total_tokens': 0}, 'web_search': {'num_requests': 0}})

# Response(...)의 괄호 안은 생성자(__init__)의 인자가 아니라, 객체의 속성(attribute)을 보기 좋게 출력한 문자열(representation)입니다.

# 3. 모델의 args로 city 전달받아. 날씨 api를 이용하여 해당 지역의 날씨 정보를 
# json으로 응답해주는 함수.. 즉. 도구로 사용될 함수 정의

def get_weather(city):
    #실제로는 여기서 해당 city의 기상청 날씨 open api 로 데이타를 가져와서 리턴함. (web data : 크롤링, 스크래핑, openapi 를 써야함) - 시간상 여기서 안함.
    return {"city":city, "temperature":31, "condition":'맑음'}

#4. 최종 응답을 위해 함수호출이 필요한지 그냥 응답이 가능한지 확인하기.
#모델이 함수호출이 필요하다고 느꼈을때.. 의 함수 항목들을 저장하는 리스트(여러개일 수도 있어서..)
# 대통령이 누구냐 ? 이에 대한 정보로 나라
#리스트 컴프리헨션 문법 : 응답 도구 중 '함수호출'인 것들만 추출. 
# function_calls = [value for value in range(1,100,10)]
# function_calls = [value*2 for value in range(1,100,10)]
function_calls = [item for item in response.output if item.type=='function_call'] # resonponse output 중에서 함수호출 타입만 가져와. "웹서치","파일서치"도 있는데 이중 함수호출만 가져오는 것이다. 
# output=[ResponseFunctionToolCall(arguments='{"city":"서울"}', call_id='call_qSL0aTfrVmEZm6DtxS5RK8I9', name='get_weather', type='function_call', id='fc_03395d7371718a9e006a5d854a6d5081988c22efb6ffa0b465', caller=None, namespace=None, status='completed')]

if function_calls: # 함수 호출이 필요하다고 판단된 경우
    # pass
    print('모델이 함수 호출로 응답해야 한다고 판단!!')

    #여러 함수가 필요하다고 판단했을 수도 있기에... 
    for call in function_calls:
        print('함수이름:',call.name)
        print('함수호출 식별ID',call.call_id)
        print('모델이 선별한 함수의 파라미터들:',call.arguments)
    
    #모델이 인식하기 편하도록.. response.output[0]의 arguments결과는 json이어서 이를 dict로 변환하여 사용
    import json
    call = response.output[0]
    args = json.loads(call.arguments) # "{'city':'서울'}" (문자열):json--> {'city':'서울'} ()

    #함수를 직접 호출하여 날씨 결과를 얻기
    weather = get_weather(args['city']) # '서울'을 전달하고 함수의 결과 받기
    print('함수 실행 결과 확인',weather) 

    #4. 함수 실행 결과(weather)를 2차 responses api에 전달하여 최종 응답 받기
    response = client.responses.create(
        model='gpt-4o-mini',
        previous_response_id=response.id, #이전 1차 응답을 참조하도록...
        #사용자의 질문은 1차에서 이미 완료되었었고... 
        #함수호출의 결과를 2차에게 제공하여 최종응답하도록
        input = [
            {
                "type":"function_call_output",
                "call_id":call.call_id,
                "output":json.dumps(weather), # dict--> ai model은 json형식을 선호(변환해야 함)
            }
        ]
    )
    #최종 응답 결과 출력
    print()
    print(response.output_text)

    #1번째 input 결과
    # [ResponseFunctionToolCall(arguments='{"city":"서울"}', call_id='call_iWGrIjgfhfVzj7rN3YS4Ms4v', name='get_weather', type='function_call', id='fc_0948923da3f90a6f006a5d9022e0d081999c6d441d80f2dba2', caller=None, namespace=None, status='completed')]

    #1차 답변 
    # 모델이 함수 호출로 응답해야 한다고 판단!!
    # 함수이름: get_weather
    # 함수호출 식별ID call_iWGrIjgfhfVzj7rN3YS4Ms4v
    # 모델이 선별한 함수의 파라미터들: {"city":"서울"}
    # 함수 실행 결과 확인 {'city': '서울', 'temperature': 31, 'condition': '맑음'}

    # 2차 답변 현재 서울의 날씨는 기온 31도이며, 맑은 하늘입니다. 더운 날씨이니 외출 시 충분한 수분을 섭취하시기 바랍니다!




else: # 함수 호출이 필요하지 않다고 느꼈다면.. 1차 응답결과로 글씨가 나옴.( 내생각 LLM 출력. )
    print('함수 호출 도구 없이 일반 응답으로 처리 가능하다고 판단!')
    print(response.output_text) 
    # 지금까지 우리는 이 부분을 봐 온것임

    # 2번 input에 대한 결과 
    # [ResponseOutputMessage(id='msg_03f150891c4c4b6a006a5d90a799648199a7f11ec72b0f1ac1', content=[ResponseOutputText(annotations=[], text='서울은 대한민국의 수도입니다.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message', phase=None)]

    # 함수 호출 도구 없이 일반 응답으로 처리 가능하다고 판단!
    # 서울은 대한민국의 수도입니다.
