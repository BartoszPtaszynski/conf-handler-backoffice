import streamlit as st

from utils.utils import load_css

css = load_css("style/styles.css")
logout_button = st.sidebar.button("Wyloguj")

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.switch_page("pages/4_Login.py")
else:
    st.header("Witamy w aplikacji konferencyjnej!")