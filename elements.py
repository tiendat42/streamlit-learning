import streamlit as st
import os

pressed = st.button("Press Me")
print(pressed)

st.title("title: Hello World")
st.header("header: Hello World")
st.subheader("subheader: Hello World")
st.markdown("markdown: Hello _World_")
st.caption("caption: Hello World")

code_example = '''
def greet(name):
    print(f"Hello {name}")
'''
st.code(code_example, language="python")

st.image(os.path.join(os.getcwd(), "static", 'IMG_0400.JPG'))
