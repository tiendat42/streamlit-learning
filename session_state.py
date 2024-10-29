import streamlit as st

st.title("Session State")

if 'counter' not in st.session_state:
    st.session_state.counter = 0

clicked = st.button("Count Me Up")
if clicked:
    st.session_state.counter += 1

reset_clicked = st.button("Reset")
if reset_clicked:
    st.session_state.counter = 0

st.write(f"Count Value: {st.session_state.counter}")
