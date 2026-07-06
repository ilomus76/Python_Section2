#파이썬의 내장된 함수.. 중.. 가장 많이 사용하는 파일입출력 기능

#1) 파일에 데이타를 저장하기 (특별한 경로가 없으면 터미널의 현재 경로) 
file = open ( 'aaa.txt',"w") #mode : w(write), a(append) , r(read)
# 덮어쓰기 
file.write('this is python programming...안녕하세요')
file.close()  
# 실행하면 파일 생김

#2) 파일의 데이터를 읽어오기.
file = open('aaa.txt','r') # rb: binary : 그림
# file = open('aaa.txt','r',encoding='UTF-8') # rb: binary : 그림
contents = file.read()
print('파일에서 읽어온 글씨:' , contents)
file.close()

print('-'*30)


#3)len() : 배열이나 , 문자열의 길이를 리턴해주는 함수
message = 'nice to meet you'
print(len(message))  #글자수

data = [10,20,30,40,50]
print(len(data))  # 요소수 

#4) max(), min()
a = max(data)
print(a)
b = min(data)
print(b)

#5) round() - 반올림
score = 87.4
score = 87.5   # 사사 오입 
print(round(score))