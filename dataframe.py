import streamlit as st
import pandas as pd
import json


df = pd.DataFrame({
    'Name': ['Dat', 'Huong', 'Ha'],
    'KNT': ['19856', '19662', '19654'],
    'Age': [26, 26, 26],
    'Position': ['Dev', 'Database', 'Lead']
})

st.title('Streamlit Element')
st.dataframe(df)

st.subheader('Data Editor')
editable_df = st.data_editor(df)
print(editable_df)

st.subheader('Static Table')
st.table(editable_df)

st.subheader('Metrics')
st.metric(label='Total Rows', value=len(df))
st.metric(label='Average Age', value=round(df['Age'].mean(), 1))

st.subheader('Dictionary and JSON')
# Open and read the JSON file
with open(r'/Users/mac/Downloads/PZ1A_2310_ET-2_22.5MY_KNT19654_reflect_ver4_20241023075614_temponarASDSADJKASHDJASHDy.json', 'r') as file:
    json_data = json.load(file)
st.json(json_data)
