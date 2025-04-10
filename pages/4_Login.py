import numpy as np
import pandas as pd
import streamlit as st

USER_CREDENTIALS = {"admin": "1234", "user": "password"}
hide_streamlit_style = """
    <style>
        .stSidebar {
            display: none;
        }
        .st-emotion-cache-1i6lr5d {
            display: none;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def authenticate(username, password):
    return USER_CREDENTIALS.get(username) == password

st.title("🔑 Logowanie")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Nazwa użytkownika")
    password = st.text_input("Hasło", type="password")
    login_button = st.button("Zaloguj")

    if login_button:
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.switch_page("Start.py")
        else:
            st.error("❌ Niepoprawne dane logowania")

elif st.session_state.logged_in:
    st.switch_page("Start.py")
