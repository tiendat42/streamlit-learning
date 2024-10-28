import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.header('Streamlit Charts Demo')

st.subheader('Chart Data')
st.table(chart_data.head(5))

st.subheader('Area Chart')
st.area_chart(chart_data)

st.subheader('Bar Chart')
st.bar_chart(chart_data)

st.subheader('Line Chart')
st.line_chart(chart_data)

st.subheader('Scatter Chart')
scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
st.scatter_chart(scatter_data)

st.subheader('Pylot Chart')
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title('Pylot Line Chart')
ax.legend()
st.pyplot(fig)
