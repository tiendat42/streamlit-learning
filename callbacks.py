import streamlit as st

if 'step' not in st.session_state:
    st.session_state.step = 1

if 'info' not in st.session_state:
    st.session_state.info = {}

def go_to_step1():
    st.session_state.step = 1

def go_to_step2(name):
    st.session_state.info['name'] = name
    st.session_state.step = 2

if st.session_state.step == 1:
    st.title('Step 1: Input')

    name = st.text_input('Enter your name')

    clicked = st.button('Next', on_click=go_to_step2, args=(name,))
    if clicked:
        st.session_state.step = 2

if st.session_state.step == 2:
    st.title('Step 2: Review')

    st.write(f'Your Name: {st.session_state.info["name"]}')

    if st.button('Submit'):
        st.success('Submitted')
        st.balloons()

    st.button('Back', on_click=go_to_step1)
