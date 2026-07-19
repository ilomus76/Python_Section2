import streamlit as st

st.set_page_config(page_title="프로그래밍 사전", layout="wide")

# -------------------------
# 데이터
# -------------------------
a={
    'A':1 ,
    'B':2,
    'C':3
}

st.write(a.keys())



docs = {

    "HTML":{

        "h1":"# h1\n\n가장 큰 제목 태그입니다.",

        "div":"# div\n\n영역을 나누는 태그입니다.",

        "table":"# table\n\n표를 만드는 태그입니다."
    },

    "CSS":{

        "color":"# color\n\n글자 색상을 지정합니다.",

        "display":"# display\n\n레이아웃을 지정합니다.",

        "flex":"# flex\n\nFlexbox 레이아웃입니다."
    },

    "JavaScript":{

        "let":"# let\n\n변수를 선언합니다.",

        "const":"# const\n\n상수를 선언합니다.",

        "function":"# function\n\n함수를 정의합니다."
    },

    "Python":{

        "with":"# with\n\n자원을 안전하게 관리합니다.",

        "enumerate":"# enumerate\n\n인덱스와 값을 가져옵니다.",

        "lambda":"# lambda\n\n익명 함수입니다."
    },

    "AI":{

        "Prompt":"# Prompt\n\nAI에게 지시하는 문장입니다.",

        "RAG":"# RAG\n\n검색과 생성을 결합한 기술입니다.",

        "Embedding":"# Embedding\n\n문장을 벡터로 변환합니다."
    }
}

# -------------------------
# 제목
# -------------------------

st.title("📚 프로그래밍 사전")

# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("📚 HTML | JAVASCRIPT | AI | ")

subject = st.sidebar.radio(
    "주제 선택",
    list(docs.keys())
)

st.sidebar.divider()

index = st.sidebar.radio(
    f"{subject} 색인",
    list(docs[subject].keys())
)

# -------------------------
# 본문
# -------------------------

st.header(subject)

st.markdown(docs[subject][index])