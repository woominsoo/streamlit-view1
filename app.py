import streamlit as st

# 제목
st.title("글자를 입력하고 출력하기")

# 입력 받기
user_input = st.text_input("여기에 글자를 입력하세요:")

# 출력
if user_input:
    st.write(f"입력한 내용: {user_input}")
