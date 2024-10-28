from datetime import date

import streamlit as st

st.title("User Information Form")

form_values = {
    'name': None,
    'height': None,
    'gender': None,
    'dob': None,
    # 'location': None
}

with st.form(key="user_form"):
    form_values['name'] = st.text_input('What is your name?')
    form_values['height'] = st.number_input('What is your height(cm)', step=1, min_value=1, max_value=200)
    form_values['gender'] = st.selectbox('Gender', ['Male', 'Female'])
    form_values['dob'] = st.date_input('Enter your Date of Birth', min_value=date(1900, 1, 1))

    submit_btn = st.form_submit_button('Submit')
    if submit_btn:
        print(form_values.values())
        if not all(form_values.values()):
            st.warning('Please fill in all fields')
        else:
            st.balloons()
            st.success('Congratulations!')
            st.write('### Infor')
            for key, value in form_values.items():
                st.write(f"{key.title()}: {value}")
