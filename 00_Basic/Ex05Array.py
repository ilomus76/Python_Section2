#배열
#파이썬 배열()  리스트 , 튜플 , 딕션너리  ,  numpy 에선 배열이라는 말을 사용
#1. list[] -- 값 추가/삭제/변경이 가능한 리스트 , 인덱스번호 자동 부여, 중복데이터 허용

aaa = [10,20,30,40]  # 각 요소 , 인덱스 0 index 
print(aaa) # 리스트를 출력하면 []로 묶어서 요소값 출력해줌. 

#요소값 사용 : 배열의 하나하나
print(aaa[0])
print(aaa[1])
print(aaa[2])
print(aaa[3])

#요소값 변경
aaa[0]=100
print(aaa)

#새로운 요소 추가
aaa.append(50) #가장 뒤에 추가 
print(aaa)

#특정 위치에 삽입하기
aaa.insert(0,1000)
print(aaa)

#요소 삭제 - remove() , del : 키워드, clear()
aaa.remove(100) #100이란느 숫자를 가진 요소를 제거
print(aaa)
# 이것을 값으로 찾아 지움

#요소의 인덱스번호로 제거하고 싶다면 ? 
del aaa[2] # 3번째 요소
print(aaa)

aaa.clear() #요소 모두 삭제 
print(aaa) 

#요소 개수 
print(len(aaa))


# PRD 문서 : 요구사항 문서 - AI가 요구사항에 따라 만들어줌. 



#5교시
#요소의 자료형이 달라도 됨. 
aaa = [10,3.14,False,'sam'] # 서로 다른 자료형이어도 됨.
print(aaa)

for e in aaa:
    print(e) 
    # 요소값 하나하나가 나온다.. JS에서는 for of 로 함.

# 리스트의 주요 기능함수들 소개. - 실제 리스트에 영향을 줌.
# 
aaa.reverse()
print(aaa) 

aaa=[4,15,7,2,16,4,10]
aaa.sort()
print(aaa)


print(aaa.index(7)) # 정렬이 되었기 때문에 index 3

print( 7 in aaa)
print(70 in aaa)
print( 7 not in aaa)
print(aaa.count(4),"개") # 4가 리스트안에 몇개 있는지. 

print(aaa.pop(2)) # 2번방 요소를 뽑아오기...
print(aaa) # 4가 하나 빠져나옴. 
aaa = [10,20,30]  # numpy 필요한 이유 
bbb =[4,5,6]
aaa.extend(bbb) # aaa배열에 bbb배열의 요소를 한방에 붙이기...
#.extend()는 잘 사용안함.. 리스트도 + 연산자로 결합가능
ccc = [700, 800,900]
print(aaa+ccc)
print(aaa) # 원본 영향 없음

aaa = aaa +ccc # aaa 변경
aaa += ccc     # aaa 변경 


#2차원 리스트
aaa = [ [10,20,30],['a','b','c'],[400,500,600]]
print(aaa[0])  # [10,20,30]
print(aaa[1])  # ['a','b','c']
print(aaa[2][1])  # 500

for list in aaa: # 3번 돔
    for e in list: #3번 돔
        print(e, end=',')
    print()
print()
#-------------------------------------

#2. tuple() - 값의 추가 / 삭제 / 변경 불가.... 나머지 리스트와 같음. 
bbb = (10,20,30)
print(bbb) # 소괄호로 출력. 튜플
print(bbb[0])
print(bbb[1])
print(bbb[2])

#튜플은 값 변경 불가
# bbb[0]=100 #에러...error
#bbb.append() # error
#  

#3. dictionary {} -인덱스 번호 대신 식별자 key를 사용하는 배열.
#값 추가/삭제/변경 가능

ccc = {'name':'sam', 'age':20, 'address':'seoul'}   # JS 에서는 {name:'sam'} # json이랑 비슷

#각 요소 사용 ( 인덱스번호 대신 ..키 사용)
print(ccc['name'])
print(ccc['age'])
print(ccc['address'])

# 리스트 , 튜플 , 딕트 전부 사용시에는 인덱스 사용

ccc['age'] = 25
print(ccc)

#새로운 식별자로 요소 추가 가능
ccc['email'] = 'aa@aaa.com'
print(ccc)

#요소 제거는 키 값으로 지워야 함 .. remove()함수는 없음. 
del ccc['email']
print(ccc)

#ccc.clear()

ccc = {'name':'sam', 'age':20, 'address':'busan'}
#특정 요소의 식별자 있는지 확인 가능
if 'name' in ccc:
    print('이름:' , ccc['name'])

#존재하지 않는 식별자를 사용하면 error

# print(ccc['tel']) #error


#if 문으로 검사하기 귀찮으면 .. get()함수 이용
print(ccc.get('name'))
print(ccc.get('tel')) # None ---에러 잆엄.


#반복문으로 요소값들 가져오기 
for key in ccc: #식별자가 전달됨. 
    print(ccc[key])

print(type(aaa))
print(type(bbb))
print(type(ccc))