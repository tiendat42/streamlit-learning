import streamlit as st
from streamlit_log import logger, UserContextFilter
import random
import time

st.title("Streamlit Logging Example")

st.write("This is a simple Streamlit app with logging.")

def login():
    user_name = random.choice(['dat', 'phuong', 'hoan'])
    email = 'email'
    print(user_name)
    return user_name, email

user_name, email = login()

UserContextFilter.update_user_info(user_name, email)

logger.info('test')

def test():
    try:
        logger.info("User clicked on the 'Log Info' button.")
        st.success("Logged info successfully!")
    except Exception as e:
        logger.error("Error when User clicked on the 'Log Info' button.", exc_info=True)


if st.button("Log Info"):
    test()

if st.button("Log Error"):
    logger.error("User triggered an error log.")
    st.error("Logged error successfully!")

