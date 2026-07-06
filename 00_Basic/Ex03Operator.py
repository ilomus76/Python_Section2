#연산자 

#1. 산술 연산자 
a = 10
b =4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # 나머지 연산자 - 나눗셈의 나머지 값
print(a//b) # 나눗셈의 몫
#목과 나머지를 한번에 구해주는 함수
x,y = divmod(10,3)
print(x)
print(y)

print(b**2) # 제곱
print(b**3) # 세제곱
print(b**(1/2)) # 제곱근 -루트 
print('-'*20)

#2. 비교 연산자
print( a> b) 
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

#파이썬은 사람의 계산처럼 비교 연산자를 연결하여 사용 가능(범위 비교 가능)
age = 20
print( 20< age < 30 )   # JS에서는 순서가 있어 안됨.

print('-'*20)


#3. 논리연산자 (비교연산에 사용할 변수가 여러개 일때.. 즉 , 조건이 여러개일때)
age = 9 
height =100
print( age> 10 and height> 120)  # 나이가 10살초과 (11살부터) 이고 키는 120초과 ! ( 두 조건 모두 맞아야 True) JS 에서는 && 로 함. 
print( age> 10 or height> 120)  # 나이가 10살초과 이거나 키는 120초과 ! ( 두 조건 중에 하나만 맞으면 True) JS 에서는 || 로 함. 

#성인이 아닌가? 
print( not age>=20 )
print('-'*20)


#4. 비트연산자 ( 숫자를 2진수로 만들고 각 진수의 자리끼리 논리연산 수행)
print(7&4) 
#   111 
# & 100
#-------
#   100    - 4(dec)

print(5|2) 
#   101 
# & 010
#-------
#   111    - 7(dec)


print('-'*20) 

#JS에 있던 증감연산자 ++ , -- 는 파이썬에 없음. 


#6. 복합대입 연산자 : =와 산술 연산자를 같이 사용하는 축약 연산자 
a =10 
# a의 값에 3을 추가하기 
a+3
print(a)  #10

a=a+3
print(a)  #13

#a 변수명을 2번 쓰기 짜증
a +=3
print(a) #16


a -=2
print(a)

a *=2
print(a) #28

a /=7
print(a) #4


#7. 삼항연산자 - JS의 ? : 는 아님. 표기볍은 if와 else
b = 'A' if(a>10) else 'B'  # 사람 말하듯이 A를 넣어 ~라면 .. 아니야 그러며 B

print (b)


#8. 형변환 연산자
a= '10'
# print(a+20) # 글씨와 숫자 덧셈 안됨 error
print(int(a) + 20) #str -> int 

a='3.14'
print(float(a) + 5.12)

print(3+5)  #산술 연산
print ( str(3) + str(5))  # 결합 연산   - 문자

