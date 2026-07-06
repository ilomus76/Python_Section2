#변수 : 데이타를 저장하는 작은 공간 ( 문자)

#변수에 담을 데이터의 종류들 마다 명칭이 있음. 이를 자료형 data type이라고 함.
#파이썬의 자료형 종류 
#1. 기본자료형 : int float str bool 
#2. 배열자료형 : list, tuple , dict , 
#3. None      : nothing ( 자바스크립트의 undefined)

#자료형별 데이타의 표기모습확인 
print(10) # int
print(3.14) # float
print(True) # bool : 대문자 , JS는 소문자
print('Hello') #str
print("Hello") #str
print("") # 한출 벌어짐. 한줄 띄기

# 변수 선언 : 그냥 변수명과 = 대입연산자로 값을 대입하면 됨. 스네이크 표기법_권장 (_ 와 - 쓰는 두가지 기법이 있다)
a= 100
print(a)

b=5.5
print(b)

c = False
print(c)

d='sam'
print(d)

e="robin"
print(e)

f=None
print(f)

# 주석 
# 변수 자료형 확인
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print("")

#변수이기에 가지고 있는 값을 바꿀 수 있음. 자료형이 달라도 됨. (동저타입언어 특성 ) 정적타입은 변수형 선언되면 안바뀜
a = 'nice ' # int -str 
print(a)
print(type(a))


#변수 하나는 1개의 값만 가질 수 있음. 그런데 여려개를 대입해도 에러 안나. 
a = 100, 200
print(a)
print(type(a)) # int가 아니라.. tuple 타입임. 즉 변수는 tuple 1개를 가진 것임.
print(a[0]) # 튜플 요소 가져오기
print(a[1])

#여러개의 변수에 여러개의 값을 한번에 대입 가능 : 머신러닝때 많이 사용
a,b = 100,200     # 튜플이 아님. . 내부적으로는 튜플인데 구조분해할당한것임. 실제로는 튜를의 구조분해할당임 
a,b = (100,200)   # 위와 같음
print(a , type(a))
print(b , type(b))


# 당연히 대입 양쪽의 객수가 같아야 함.
# a,b = 100 # error
# a,b = 100,200,300 #error  JS에서는 내가 원하는 만큼 가져올수 있었음. 

# 문자열 타입 데이터만의 연산자 + , * ,[]
print("aa" + "bb") # 산술 연산이 아니라.. 결합 연산
print("Hello" *3) #반복 연산자 - "hello"를 3번 붙이기
s = "Good" * 5  # Good이라는 글자를 5번 붙여서 s에 대입
print(s)

#문자열 인덱싱/슬라이싱 연산자[] 
print("Hellow world"[1]) # 1번 인덱스 위치의 한글자 추출 - 'e'
print("Hellow world"[1:7]) # 1번 인덱스부터 7번전까지 위치의 글자 추출 - 'ello w'
print("Hellow world"[1:]) # 1번 인덱스부터 끝까지 위치의 글자  추출 - 'ello world'
print("Hellow world"[:7]) # 처음부터 7번전까지 위치의 글자  추출 - 'ello world'
print("Hellow world"[-1]) # 뒤에서 첫번째 인덱스 한글자 추출 -'d' : 머신러닝에서 많이 사용
print("Hellow world"[-5]) # 뒤에서 5번째 인덱스 한글자 추출 -'w'
print("Hellow world"[:-1]) # 마지막 요소만 빼고 모두 추출 -'Hellow Worl'  : 이것도 많이 사용     : 앞이 요인 뒤가 결과 대부분의 표가 이러함.. 앞에것은 종속변수 뒤에 있는 것이 독립변수 ...


#3교시
#문자열의 글자수를 확인
s = 'maching learning'
print(len(s))

# 문자열데이터는 가장 많이 사용하는 데이터 유형
# 그래서 문자열이 가진 주요 기능함수들 확인
print("{}만원".format(5000))
print("Hello".upper())
print("Hello".lower())
print("     Hello     ".strip()) # 양쪽 공백만 제거 
print("     Hello  world   ".strip()) # 양쪽 공백만 제거  # 검색창에 사용자 입력할때 데이타 베이스에 이렇게 저장되면 못찾음. 그래서 이 기술이 필요..
print("Hello world. android. ios. web".find('ios')) #찾은 글자의 첫번째 자리 인덱스번호 
print("Hello world. android. ios. web".find('mac')) # 없으면 -1 : JS와 같음. 
#csv 데이터에서 , 기준으로 글씨를 분리시키기
csv = "sam,20,seoul" 
values = csv.split(',') # comma split vlaue
print(type(values))  #list
print(values[0] , type(values[0]))
print(values[1] , type(values[1]))
print(values[2] , type(values[2]))

#특정 글자가 포함되어 있는지 여부 (True / False)
print("sam" in csv) 
print("robin" in csv) 

# 문자열 데이터를 만들때 3따옴표... ''' , """
print('''

이 안에 쓰면.. 
써 있는 고대로 .. 줄바꿈도 가능


''')

# print('ddkfj' \)

# 위 3따옴표는 함수의 doc string 에 활용하는 경우가 많음 (doc string: 함수를 설명하는 글씨 -- AI가 이 글씨를 확인하여 답변에 활용할 수 있음 -구글이 이걸 함. )
# 사용자가 이 함수를 읽으면 이렇게 해 라고 하여 사용
# AI에게 제공하는 프롬프트를 자세히 길게 쓸때 많이 사용 

prompt ="데이터 분석해줘,"
prompt_eng = '''

[역할]
너는 전문 데이터 분삭야..
[제한사항]
초등학생도 이해하게 분석결과를 알려쥐

'''


#3.5버전이상에서 새로 등장한 자료형 힌트
score: int =10 # score변수가 int 형을 가지도록 만들었다고 표식!

# def aaa(message:str , a:int, b:bool ,c):   # 변수를 str를 받을 거야.. .. 하지만 이것이 에러가 나지 않는다. 날수도 있음.  
#     print(message)