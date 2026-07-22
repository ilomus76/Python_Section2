#!/usr/bin/env python
# coding: utf-8

# In[1]:


#주피터 노트북: 파이썬의 쉘환경 + 코드 파일 작성을 동시에 수행하고 코드와 실행결과를 하나의 파일에 저장할 수 있는 웹 기반 개발환경
#파일 확장자 .ipynb

# 이런 코드를 작성할 수 있는 이 박스를 cell(셀) 이라고 부름.


#파이썬 인터렉티브쉘처럼 사용가능
print('Hello Jupyter notebook')

#실행은 어떻게 시키나? : 위의 run 메뉴의 run selected cell


# In[2]:


name= 'sam'
print(name)


# In[3]:


100


# In[4]:


50+30


# In[5]:


#실행을 해야 왼쪽 번호가 부여됨 

# cell 실행모드 3가지  , 엔터는 줄바꿈, ctrl+엔터 : 새로운 줄이 생기지 않음
# alt +endter 는 아래에 빈 줄이 있어도 생기고 shift +enter는 아래 줄이 있으면 안생김
print('Hello') 


# In[6]:


print('Hello') 


# In[7]:


#셀의 실행순서대로 코드가 실행됨. 작성된 순서가 아님.


# In[8]:


#[1] 변수 선언
num=100


# In[9]:


#[2] 변수 연산
num += 50


# In[10]:


#[3] 연산결과 출력
print(num)


# In[11]:


#셀을 개별 덩어리로 생각한다. 


# In[12]:


#에러 발생위치 확인
name = 'robin'
print(name)
print(nice to meet you)


# In[16]:


#모듈 사용하기
import random
num = random.randint(1,46)
print(num)


# In[20]:


#자동 완성안됨.  하려면 tab을 눌러라.  ? : 함수가 뭔지 알려줌 ?? 좀더 자세히 알려줌. 
#num = random.randint? # ?를 사용하면 함수의 설명을 볼수 있음. --실행

get_ipython().run_line_magic('pinfo', 'random.randint')
help(random.randint)


# In[18]:


#[]안에 숫자가 있어야 실행완료.. 혹시 * 이면 실행중 
import time 
for i in range(10): # 0부터 9까지
    print(i)
    time.sleep(0.5)


# In[19]:


# 주피터 노트북의 장점 - 셜명을 작성하기 위한 cell을 만들 수 있음.
# 코드 cell이 아닌 마크다운문법을 사용할 수 있는 설명 cell을 사용해보기


# 마크다운 문법을 작성할 수 있어요. 실행은 코드처럼 ctrl+enter 로 실행하면 마크다운을 랜더링한 결과 화면이 보여짐. 
# 마크다운 문법이기에 엔터를 친다고 줄바꿈되지 않음. 줄바꿈 하려면 br 같은 태그같은 역할의 문법.  
# 띄어쓰기  2번.
# 
# 이렇게..
# 
# 마크다운 언어의 제목요소 표시 h1~h6를 대체.. # 의 개수로 ( 띄어쓰기 있어야 함. )
# # 제목1
# ## 제목2
# ### 제목3
# #### 제목4
# ##### 제목5
# ###### 제목6
# ####### 제목7은 없음. 
# 
# **bold** 또는 __bold__ 를 통해 strong(강하게)표시 가능    
# *italic* 또는 _italic_ 를 통해 emphasize(강조) 표시 가능
# *** bold and italic*** 또는 ___bold+italic 표시 가능
# 
# 블로그에도 마크다운을 쓸수 있다. 

# >인용구를 만들 수도 있음.
# >인용구도 공배문자 2개가 있어야 줄바꿈 됨.  이렇게
# 
# ---
# 
# ### unordered list
# - 리스트1
# - 리스트2
# - 리스트3
# 
# ### ordered list
# 1. aaa
# 2. bbb
# 3. ccc
# 
# 순서가 있는 리스트는 모두 1을 써도 자동 증가됨.  
# 1. aaa  
# 1. bbb  
# 1. ccc  
# 
# *** 
# # 이것도 줄 그어짐. 
# 

# ## 이미지 표시
# - windows 에서 print screen으로 이미지 캡쳐하여 붙여넣기 하면 이미지가 표시됨 
# ![image.png](attachment:b2b756a0-a7b0-451b-a744-e28edd9c34f0.png)
# 
# 
# - 특정 이미지의 경로를 직접 지정(스타일지정 {} 는 gitHub에서는 인식되고 .. 노트북에서는 안됨)
# 
# ![모아나](./moana01.jpg){: width="100" height="100"}
# 
# 
# - 크기 지정을 하려면 아크업언어사용 (마크업은 다 됨)
# <img src="./moana01.jpg" alt="모아나" width="100">
# 

# ## 마크다운 링크(anchor)요소
# [네이버](https://www.naver.com)
# 
# ---
# 
# 
# ## 유투브 영상 링크 
# 유튜브 동영상의 마우스 우클릭하여 **소스코드 복사**를 누르고 cell에 붙여넣기 
# <iframe width="1337" height="752" src="https://www.youtube.com/embed/UkFLk0-xf58" title="[MV] 헌트릭스(HUNTR/X) - Golden l 한글자막 뮤직비디오" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
# 
# 
# iframe 의 사용은 코드 cell에서  %%html을 입력한 다음 붙여넣기해야 함.

# In[24]:


get_ipython().run_cell_magic('html', '', '<iframe width="480" height="280" src="https://www.youtube.com/embed/UkFLk0-xf58" title="[MV] 헌트릭스(HUNTR/X) - Golden l 한글자막 뮤직비디오" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>\n\n')


# In[ ]:


# 노트북 파일 .ipynb 파일을 다른 형태로 변환하여 추출 및 다운로드 가능. 

#1. html 파일로 다운로드 ( 파이썬 개발환경이 없는 곳에서 코드와 실행결과 확인가능)
#2. pdf 파일로 다운로드 ( 파이썬 개발환경이 없는 곳에서 코드와 실행결과 확인가능)
#3. .py 파일로 다운로드 ( 코드가 아닌 cell 들은 모두 주석처리됨)

