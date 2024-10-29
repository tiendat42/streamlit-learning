import streamlit as st

st.sidebar.title("This is a new Sidebar")
st.sidebar.write("You can place element in Sidebar")

with st.sidebar.form(key='user_form'):
    st.text_input("This is the form")
    st.form_submit_button("Click me")
    st.sidebar.success("This is the sidebar")

tab1, tab2, tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])

with tab1:
    st.write("This is the first tab")
with tab2:
    st.write("This is the second tab")
with tab3:
    st.write("This is the third tab")


col1, col2 = st.columns(2)
with col1:
    st.subheader("This is the first col")
with col2:
    st.subheader("This is the second col")

with st.container(border=True):
    st.subheader("This is the Container with border")
    st.write('This is content inside Container')

placeholder = st.empty()
placeholder.write('Placeholder Row')

if st.button('Place Holder'):
    placeholder.write('Placeholder Updated')

with st.expander('Expander for more detail'):
    st.subheader('This is content inside Expander')

    st.button('Tool Tip Button', help='This is a tool tip')
