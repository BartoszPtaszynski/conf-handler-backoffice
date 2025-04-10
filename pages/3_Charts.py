import streamlit as st
from utils.utils import load_css

css = load_css("style/styles.css")

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
logout_button = st.sidebar.button("Wyloguj")