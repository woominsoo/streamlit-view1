import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

st.title("tmdh-business")
st.write("이 사이트는 간단한 설명을 위한 예제입니다.")
st.write("")

def home_page():
    st.title("첫 번째 페이지")
    st.title("수제제작 젓가락")
    st.write("가격 : 59,000WON")
    if st.button("구매하기"):
        st.session_state.page = "next"

def next_page():
    st.title("구매페이지")
    st.write("항목 : ")
    if st.button("둘러보기"):
        st.session_state.page = "home"

if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "next":
    next_page()
