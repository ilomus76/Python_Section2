#함수 - 코드가 써져있는 영역... 함수 호출을 통해 코드가 실행되도록...

#함수 정의
def show():
    print('show function')
    print('얀녕하세요')

#함수 호출
show()
show()


# 파라미터를 전달받는 함수

def output(a,b):
    print('a:',a)
    print('b:',b)

output(10,20)
# output(100) # error

# output(10,20,30) #error

#혹시 같은 이름의 함수를 또 점의하면.. 이전 함수는 없어짐.(단 JS와는 다르게 위에 코드까지는 이전 함수 동작함 )
#JS는 함수가 밑에 있어도 위로 올려 선언적 함수 표현 . 호이스트..


def output():
    print('이건 새로 만든  output function')

output()
# output(10,20) #error    기존의 함수가 나중것으로 바뀌었음.

# 파라미터에 default value지정 가능
def display(a=1,b=2):
    print('a:', a)
    print('b:',b)

display(100,200)
display(100)
display()
display(b=200)  


# 리턴을 해 주는 함수 
def sum(a,b):
    return a+b
num = sum(5,3)
print(num)

#return 은 함수영역의 실행을 멈추고 돌아가라는 키워드
def aaa():
    print('aaa function')
    return # 이 뒤로 함수영역에 써있는 글씨는 실행안됨.  
    print('aaaaaaa') 

aaa()

#return 할때 값을 주지 않았는데.. 혹시 대입받으면? 뭐가 올까요? 안옴.. 안오면 None
m = aaa()
print(m)

# return 에 값을 여러개 할수 없지ㅏㄴ.. 만약 여려개를 쓰면.. 자동으로 튜플로 묶어서 리턴함


def bbb():
    return 100,200,300


n1,n2,n3 = bbb() #구조 분해 할당 


print(n1, n2, n3)


#람다함수 lamda 함수...   -- 함수 코드의 간단 표현 [ JS 의 화살표함수와 비슷]
#1) 간단한 함수
def eee(n):
    return n*10   # A


num = eee(3)
print(num)

#위의 함수가 너무 짧아 줄여서 써보자

#2) 람다함수로 줄이자
eee = lambda n:n*10  # B  A와 B는 동일  , 화살표 함수와 같음. 
num = eee(4)   
print(num)