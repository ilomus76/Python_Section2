#!/usr/bin/env python
# coding: utf-8

# # Numpy
# Numerical Python의 약자로 과학 및 공학 분야에서 사용되는 오픈 소스 파이썬의 라이브러리 
# 
# - 대량의 데이터를 다루는 ** 배열을 만들어주는 라이브러리**
# - 파이썬 배열(리스트)와 다르게 **수학적인 행렬의 사칙연산을 수행** 해줌

# In[1]:


# 설치.. 
# 설치를 해야 한다면 pip install numpy , 하지만 anaconda 에서는 설치가 되어 있으니 안해도 됨.


# ### 1. 일반적인 파이썬 배열(리스트)

# In[2]:


aaa=[10,20,30] 
bbb = [4,5,6]

print (aaa)
print (bbb)


# In[3]:


#파이썬 리스트의 덧셈을 하면..수학계산이 아니라 결합연산
ccc = aaa + bbb
print(ccc)


# In[4]:


#수학적 계산이 아니라 결합이 됨.
#자료형 확인 
print(type(aaa))


# ### 2. numpy 배열

# In[5]:


import numpy as np
aa=np.array([10,20,30])
bb=np.array([4,5,6])

print(aa)
print(bb)


# In[6]:


#배열의 사칙연산이 수학적으로 수행됨
cc = aa + bb
print(cc)


# In[7]:


#실제 수학의 행렬 계산이 되었음. 
#배열의 요소 개수 확인
print(len(aa))
print(len(bb))
print(len(cc))


# In[8]:


# 단 , 넘파이 배열을 사용할때는 가급적 사이즈를 .shape 속성으로 확인하는 것을 권장. 
# 이유는 행렬 구조로 알려주기때문에...
print(aa.shape)
print(bb.shape)
print(cc.shape) # 튜플로 (행,열)개수를 표시.. 단 현재 1차원이니..값이 하나만...


# In[9]:


#자료형 확인
print(type(aa))


# In[10]:


# <class 'numpy.ndarray'> : n dimension array. 


# ### 3. 다차원 넘파이 배열

# In[17]:


aaaa= np.array([[10,20,30,40],[5,6,7,8]])
print(len(aaaa)) # 2 <--행개수
print(len(aaaa.shape)) # 튜플 (행, 열)

bbbb = np.array([[100,200,300,400],[50,60,70,80]])
print(bbbb.shape)

#사칙연산 가능
cccc = aaaa + bbbb
print( cccc.shape )
print( cccc )


# In[18]:


#사칙연산 모두 가능
print( aaaa - bbbb )
print ( aaaa * bbbb) #요소별 곱셈
print( aaaa / bbbb) #요소별 나눗셈


# In[20]:


# 연산 주의! 행령의 개수가 다르면 에러!!
dddd = np.array([10,20,30,40],[500,600]) # 정형데이타만 되어서 에러가 남. 


# In[21]:


#연산하는 행렬의 개수도 맞아야 함. 
eeee = np.array([ [10,20], [50,60] ])
ffff = aaaa + eeee   # 이것도 행렬의 갯수가 안맞아 에러


# In[23]:


# 수학적 행렬의 곱셈 - 1차원 배열일때때는 내젹 곱(dot), 2차원 배열일 때는 수학의 행렬 곱셈을 수행

#2차원 배열
A  = np.array([
    [1,2],
    [3,4]
])

B  = np.array([
    [5,6],
    [7,8]
])

print(A@B) # 행렬 곱
#or
print(np.matmul(A,B))



# In[24]:


# 1차원 배열일 경우에는 내적곱(요소끼리 곱하여 덧셈) -- 벡터끼리 내적을 하면 --> 스칼라값
C = np.array([1,2,3,4]) # 벡터
D = np.array([5,6,7,8]) # 벡터

print( np.dot(C,D)) # 스칼라 


# In[25]:


### 4. 넘파이 주요 메소드 와 속성 -- 판다스는 넘파이를 가지고 만든것임


# In[45]:


#1. 특정 규칙을 가진 값들로 배열을 생성해주는 기능메소드
aaa = np.zeros(5)  # 소수점숫자 5개로 만듦.
print(aaa)


# In[27]:


bbb = np.ones(5)
print(bbb)


# In[28]:


# true, false 는 데이타 분석에 안맞음. 그래서 0, 1로 바뀌어야 하므로 많이 사용

ccc = np.full(5,7) # 7로 5번..
print(ccc)


# In[30]:


ddd = np.arange(5) # 0~4
print(ddd)


# In[31]:


eee = np.arange(2,20,3) # start , < end , step
print(eee)


# In[32]:


fff = np.random.random(3) # 랜덤값 3개 (0.0~1.0사이 숫자)
print(fff)


# In[34]:


ggg = np.linspace(0,100,3) #선형적인 간격을 만들어 줌. , 0부터 100까지의 범위안에서 균등 3분할 지점 값들 
print(ggg)


# In[37]:


#2. 배열 속성 및 정보
# 배열의 행,열 크기 정보
aaa = np.array([10,20,30]) # 1차월 
print(aaa.shape)

bbb = np.array([ [ 1,2,3],[4,5,6] ]) # 2차원 
print(bbb.shape)


# In[38]:


#요소의 총 개수
print(aaa.size)
print(bbb.size)


# In[39]:


#파이썬의 len()함수는 차원 상관없이 요소의 개수
print(len(aaa))
print(len(bbb)) #2행 <-- 행개수

#행개수를 확인하는 또 다른 방법
print(bbb.shape[0]) #행


# In[41]:


# 배열의 원소의 자료형 
print(aaa.dtype) 
print(bbb.dtype)
print(type(aaa))
print(type(bbb))


# In[42]:


ccc = np.array([3.14, 4.5, 7.89])
print(ccc.dtype)


# In[43]:


ddd = np.array(['sam','robin','hong'])
print(ddd.dtype) # <U5 유니코드 5보다 작다.


# In[44]:


#배열을 만들때 자료형을 지정할 수 도 있음. 다른 데이터 저장은 안됨.
eee = np.array(['sam','robin','hong'],dtype=str) # dtype = int 를 사용하면 에러...!


# In[46]:


#넘파이 배열을 기본적으로 같은 자료형만 저장 가능.. 다른 자료형을 함게 저장하면... 전부 문자
fff = np.array([10,20,30,3.14,True,'sam'])
print(fff.dtype) #<U32 <유니코드 32- 문자열 . 전부 문자로 만듦


# In[48]:


#배열의 차원 정보 확인 
aa = np.array(12) # 스칼라 (0차원)
aa.ndim


# In[50]:


#배열의 차원 정보 확인 
bb = np.array([1,3,5]) # 벡터 (1차원)
bb.ndim


# In[52]:


cc = np.array([[2,6,4],[1,3,5]]) #매트릭스 (행렬 ) -2차원 배열
cc.ndim


# In[53]:


dd = np.array([
    [[2,6,4],[1,3,5]],
     [[2,6,4],[1,3,5]]       
]) #3차원 배열 (텐서 Tensor) 
dd.ndim


# In[54]:


#수학 및 통계 연산 기능 메소드 (함수)
#10명의 학생 성적 데이터
scores = np.array([ 70,80,64,73,42,98,27,40,85,100])


# In[55]:


#요소들의 총합 구하기 [ 2가지 방법]
print('총점:',scores.sum())
print('총점:',np.sum(scores))


# In[57]:


#요소들의 평균 구하기 [ 2가지 방법 ] 
print('평균:',scores.mean())
print('평균:',np.mean(scores))


# In[58]:


#요소의 최대값 / 최소값 구하기 [2가지 방법]
print('최대값:',scores.max())
print('최대값:',np.max(scores))
print('최소값:',scores.min())
print('최소값:',np.min(scores))


# In[59]:


# 조건에 따라 원소들의 결과값을 계산하는 기능(파이썬 삼항연사자 + 반복문)
#예) 60점 이상은 'pass' 아니면 'fail'
result =np.where(scores >60, 'pass', 'fail') #조건 ,참일때 값, 거짓일때 값
print(result)


# In[62]:


# 배열 결합 (파이썬의 리스트처럼) 
aaa = np.array([1,2,3])
bbb = np.array([4,5,6])

result = np.concatenate((aaa,bbb)) #튜플로
print(result)


# In[63]:


# 2차원 배열일때는 .. 행으로 불일지 ... 열로 붙일지
a = np.array([ [1,2],
            [3,4]])

b = np.array([ [5,6],
            [7,8]])


# In[64]:


#행 기준 연결(위아래)
result1 = np.concatenate((a,b),axis=0) # # axis =0 행방향..으로 내려가면서 붙이기....
print(result1)


# In[66]:


#열 기준 연결(좌우)
result2 = np.concatenate((a,b),axis=1) # # axis =1 열방향..오른쪽으로 내려가면서 붙이기....
print(result2)


# In[67]:


# 인덱싱 및 슬라이싱

#1번 학생(0번 인덱싱)의 성적 데이터
first_student = scores[0]

#2~7번 학생 (슬라이싱)[ 인덱스 번호로는 2~6]
middle_student = scores[2:7]

print(first_student)
print(middle_student)


# In[72]:


# 불리언 인덱싱 - 기준 점수 이상인 학생만 추출
# 80점 이상인 학생들의 성적만 추출
high_scores = scores[scores>=80] # 조건값이 true인 요소들만 인덱싱
print(high_scores)
print(high_scores.mean())
print(len(high_scores))

#EDA 분석에 위의 개념이 중요.


# In[73]:


# 배열의 차원을 변경 시켜주는 기능 reshape()
# 1차원 → 2차원 (reshape)
# 5명 학생 × 7일 = 35개 점수
scores_1d = np.array([
    80, 75, 90, 85, 87, 92, 78,
    70, 65, 75, 80, 82, 85, 79,
    90, 88, 91, 94, 96, 95, 93,
    60, 65, 70, 72, 74, 76, 78,
    85, 87, 88, 90, 92, 91, 89
])

print(scores_1d)


# In[75]:


#(학생수,날짜수) 형태로 변경
scores_2d=scores_1d.reshape(5,7) # 5행 7열로 만들어 줘.


# In[76]:


# 행, 열중 한쪽만 지정하고.. 나머지는 알아서 계산되도록 설정
# scores_2d=scores_1d.reshape(5,-1) # 5행 ? 열로 만들어 줘.  => 정형 데이타를 다루기에 딱 떨어지지 않으면 에러
scores_2d=scores_1d.reshape(-1,7) # ?행 7 열로 만들어 줘.  => 정형 데이타를 다루기에 딱 떨어지지 않으면 에러
print(scores_2d)


# In[79]:


#차원을 변환하면.. 좋은점.. 분석하기 용이해짐
student_aver = scores_2d.mean(axis=1) # 기준 계산 - - 옆으로 가면서 계산 
print(student_aver,len(student_aver))

#날짜별 평균 점수
day_aver = scores_2d.mean(axis=0) # 기준 계산 - - 아래로 가면서 계산 
print(day_aver,len(day_aver))



# In[ ]:




