# openai responses api tools 로 검색해서 가봐라.

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

#response api 호출
response = client.responses.create(
    model='gpt-4o-mini',
    # instructions='질문에 대한 답변을 간단하게 응답해. 한글기준 100글자안에 뭐든 대답해. tools가 지정되어있다면 가급적 tools 사용을 권장함',  # 이 지침에 의해 응답결과 줌
    instructions='질문에 대한 답변을 간단하게 응답해. 한글기준 100글자안에 뭐든 대답해. 현재 시점에 대한 질문이 있다면 tools를 사용한 결과를 먼저보여주고. 답변을 보여쥐.',  
    # input='대한민국의 지금 대통령이 누구야?',
    input='국제규격의 축구장 크기는 몇 cm야?',   # 자기가 학습한것이 아니라 벡터 스토어에 있는 것을 이용해서 답을 함. 
    #하이퍼파라미터
    max_output_tokens=5000,

    #도구 연결 - 응답에 참고할 도구를 지정
    tools = [
        #1) 웹 검색 도구 사용
        # {'type':'web_search'},
        #2)파일검색 도구 사용 (문서를 vector db에 저장하고 검색하여 답변하는 RAG 시스템)
        # 금요일에 리트리버까지 만들었는지 이제 쉽게.
        # {'type':'file_search','vector_store_ids':['문서1','문서2','문서3'..]}, #
         {'type':'file_search','vector_store_ids':['vs_6a5d7ca88c64819183ee30953904b54d']}, #벡터스토어 아이디
         #openai api 플랫폼 사이트에 문서를 업로드하여 클라우드 환경의 RAG 구축가능 
         # vector는 하루마다 보관료 비용이 지불됨. GB당 0.1정도됨(실습 후 삭제!!!!)
         # openai -> api플랫폼 -> storage -> vector stores -> 축구규칙정리.pdf를 올려라.
         # codex : 바이브 코딩 
        #  결과 : Response(id='resp_02ba2865cb487054006a5d7ebfad088199b4e458af8e68081e', created_at=1784512191.0, error=None, incomplete_details=None, instructions='질문에 대한 답변을 간단하게 응답해. 한글기준 100글자안에 뭐든 대답해. 현재 시점에 대한 질문이 있다면 tools를 사용한 결과를 먼저보여주고. 답변을 보여쥐.', metadata={}, model='gpt-4o-mini-2024-07-18', object='response', output=[ResponseFileSearchToolCall(id='fs_02ba2865cb487054006a5d7ec074108199997e53426ae7388a', queries=['국제규격 축구장 크기', '축구장 크기', '축구장 국제규격'], status='completed', type='file_search_call', results=None), ResponseOutputMessage(id='msg_02ba2865cb487054006a5d7ec30768819993bed2111aba61f4', content=[ResponseOutputText(annotations=[AnnotationFileCitation(file_id='file-XfvxoNDZ96ee74bmfoX98c', filename='축구규칙정리.pdf', index=109, type='file_citation')], text='국제규격 축구장 크기는 터치라인 길이가 최소 100m(약 10,000cm)에서 최대 110m(11,000cm), 골라인 길이는 최소 64m(약 6,400cm)에서 최대 75m(7,500cm)입니다.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message', phase=None)], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[FileSearchTool(type='file_search', vector_store_ids=['vs_6a5d7ca88c64819183ee30953904b54d'], filters=None, max_num_results=20, ranking_options=RankingOptions(hybrid_search=None, ranker='auto', score_threshold=0.0))], top_p=1.0, background=False, completed_at=1784512195.0, conversation=None, max_output_tokens=5000, max_tool_calls=None, moderation=None, previous_response_id=None, prompt=None, prompt_cache_key=None, prompt_cache_options=None, prompt_cache_retention='in_memory', reasoning=Reasoning(context=None, effort=None, generate_summary=None, mode=None, summary=None), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=4620, input_tokens_details=InputTokensDetails(cache_write_tokens=0, cached_tokens=0), output_tokens=116, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=4736), user=None, billing={'payer': 'developer'}, frequency_penalty=0.0, presence_penalty=0.0, store=True, tool_usage={'image_gen': {'input_tokens': 0, 'input_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'output_tokens': 0, 'output_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'total_tokens': 0}, 'web_search': {'num_requests': 0}})
        # 실제로는 회사에서는 자기들 시스템에 RAG를 쓰기 때문에 굳이 필요없다. 
    ],
    #웹 검색 도구를 지정했다고 무조건 사용하지 않음. 도구를 사용할지 여부를 LLM이 판단함. - 이래서 결과가 tool을 썼다고 아직 대통령이 윤석렬이라고 나오는 것이다. 
    #판단에 대한 기준을 설정!
    # tool_choice='required', #댭변할때 무조건 도구를 사용해라 ! (권장하지 않음) # 'none' # 안쓰겠다. 'auto': 자동으로  'required :댭변할때 무조건 도구를 사용해라
    # 웹검색이 필요없어도 무조건 웹검색 사용하며 토큰을 소진함. !
    tool_choice='auto', #default 권장 -- 대신 지침으로 도구 사용 유도...      # 이렇게 하더라도 계속 윤석렬이 나올수 있다. 이럴 경우 프럼프트를 더 잘써야 한다. 


)
#응답결과 출력
print(response.output_text)
print("="*20)
print(response) # 토큰 사용량등 메타데이터까지 출력. 여러속성들.

# 도구 tool 이 없을때 답변 
# Response(id='resp_0ae56f05ea4b7da5006a5d766b874481989644adf0717d61c3', created_at=1784510059.0, error=None, incomplete_details=None, instructions='질문에 대한 답변을 간단하게 응답해. 한글기준 100글자안에 뭐든 대답해', metadata={}, model='gpt-4o-mini-2024-07-18', object='response', output=[ResponseOutputMessage(id='msg_0ae56f05ea4b7da5006a5d766d5288819899c118eeba3ec84a', content=[ResponseOutputText(annotations=[], text='대한민국의 현재 대통령은 윤석열입니다.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message', phase=None)], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[], top_p=1.0, background=False, completed_at=1784510061.0, conversation=None, max_output_tokens=5000, max_tool_calls=None, moderation=None, previous_response_id=None, prompt=None, prompt_cache_key=None, prompt_cache_options=None, prompt_cache_retention='in_memory', reasoning=Reasoning(context=None, effort=None, generate_summary=None, mode=None, summary=None), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=49, input_tokens_details=InputTokensDetails(cache_write_tokens=0, cached_tokens=0), output_tokens=12, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=61), user=None, billing={'payer': 'developer'}, frequency_penalty=0.0, presence_penalty=0.0, store=True, tool_usage={'image_gen': {'input_tokens': 0, 'input_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'output_tokens': 0, 'output_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'total_tokens': 0}, 'web_search': {'num_requests': 0}})

# 도구 tool가 있을때 답변
# Response(id='resp_091489f20a5afa47006a5d7707990481998db6121afdce705b', created_at=1784510215.0, error=None, incomplete_details=None, instructions='질문에 대한 답변을 간단하게 응답해. 한글기준 100글자안에 뭐든 대답해', metadata={}, model='gpt-4o-mini-2024-07-18', object='response', output=[ResponseFunctionWebSearch(id='ws_091489f20a5afa47006a5d77083ad88199a14c540ac1204ff9', action=ActionSearch(type='search', queries=['current president of South Korea'], query='current president of South Korea', sources=None), status='completed', type='web_search_call'), ResponseOutputMessage(id='msg_091489f20a5afa47006a5d770935e481998bf909a8dfd9bd52', content=[ResponseOutputText(annotations=[], text='2026년 7월 20일 현재, 대한민국 대통령은 이재명입니다. ', type='output_text', logprobs=[])], role='assistant', status='completed', type='message', phase=None)], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[WebSearchTool(type='web_search', filters=None, search_context_size='medium', user_location=UserLocation(city=None, country='US', region=None, timezone=None, type='approximate'), return_token_budget='default', search_content_types=['text'])], top_p=1.0, background=False, completed_at=1784510218.0, conversation=None, max_output_tokens=5000, max_tool_calls=None, moderation=None, previous_response_id=None, prompt=None, prompt_cache_key=None, prompt_cache_options=None, prompt_cache_retention='in_memory', reasoning=Reasoning(context=None, effort=None, generate_summary=None, mode=None, summary=None), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=8174, input_tokens_details=InputTokensDetails(cache_write_tokens=0, cached_tokens=0), output_tokens=36, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=8210), user=None, billing={'payer': 'developer'}, frequency_penalty=0.0, presence_penalty=0.0, store=True, tool_usage={'image_gen': {'input_tokens': 0, 'input_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'output_tokens': 0, 'output_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'total_tokens': 0}, 'web_search': {'num_requests': 1}})



