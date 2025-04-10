import streamlit as st


def main():
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Individual Checker', icon='🔥')
        st.page_link('pages/1_Conference_data.py', label='Competition Checker', icon='🛡️')
        st.page_link('Start.py', label='Competition Checker', icon='🛡️')

    st.title(f'🔥 Individual Checker')



if __name__ == '__main__':
    main()