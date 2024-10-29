import streamlit as st

st.button('test1', key='test1')
st.button('test1', key='test2')

if 'slider' not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider('Set min value', 0, 50, 25)

slider_value = st.slider('Slider', min_value, 100, st.session_state.slider)

if 'checkbox' not in st.session_state:
    st.session_state.checkbox = False
if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

st.write('Your session:', st.session_state.user_input)

checked = st.checkbox('Show Input Field', value=st.session_state.checkbox)

if checked:
    user_input = st.text_input('Enter your name', value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.user_input

st.write('Your Input:', user_input)
