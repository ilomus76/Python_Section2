import streamlit as st

# ---------------------------------------
# Python 기능 설명 함수
# ---------------------------------------
def explain_python(keyword):
    """
    입력받은 Python 기능에 대한 설명을 문자열(Markdown)로 반환한다.
    """

    docs = {

        "with": """
# with

## 1. 한 줄 정의
`with`는 자원을 안전하게 사용하고 자동으로 정리하기 위한 문법입니다.

## 2. 언제 사용하는가
- 파일 열기
- 데이터베이스 연결
- Lock 사용
- Streamlit의 컨테이너 사용

## 3. 기본 문법

```python
with open("sample.txt") as f:
    text = f.read()
```

## 4. 장점

- close()를 자동으로 호출
- 예외가 발생해도 안전
- 코드가 간결해짐
""",

        "for": """
# for

## 1. 한 줄 정의

반복 가능한 객체를 순회하는 반복문입니다.

## 2. 기본 문법

```python
for i in range(5):
    print(i)
```

## 3. 실행 결과

```
0
1
2
3
4
```
""",

        "enumerate": """
# enumerate

## 1. 한 줄 정의

인덱스와 값을 동시에 가져오는 함수입니다.

## 2. 예제

```python
names = ["Kim","Lee","Park"]

for idx, name in enumerate(names):
    print(idx, name)
```
""",

        "lambda": """
# lambda

## 1. 한 줄 정의

이름이 없는 간단한 함수를 만드는 문법입니다.

## 2. 예제

```python
add = lambda x,y : x+y

print(add(3,5))
```
"""
    }

    return docs.get(
        keyword.lower(),
        f"# {keyword}\n\n등록되지 않은 Python 기능입니다."
    )


# ---------------------------------------
# Streamlit 화면
# ---------------------------------------

st.set_page_config(
    page_title="Python 기능 설명기",
    page_icon="🐍"
)

st.title("🐍 Python 기능 설명기")

keyword = st.text_input(
    "Python 기능을 입력하세요",
    placeholder="예) with, for, lambda, enumerate"
)

if st.button("설명 보기"):

    if keyword.strip() == "":
        st.warning("기능명을 입력하세요.")
    else:

        result = explain_python(keyword)

        st.markdown(result)