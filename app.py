import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

def home_page():
    st.title("첫 번째 페이지")
    if st.button("다음 페이지로 이동"):
        st.session_state.page = "next"

def next_page():
    st.title("두 번째 페이지")
    st.write("여기는 두 번째 페이지입니다!")
    if st.button("첫 번째 페이지로 돌아가기"):
        st.session_state.page = "home"

if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "next":
    next_page()

st.title("tmdh-business")
st.write("이 사이트는 간단한 설명을 위한 예제입니다.")
st.write("")
