import streamlit as st

x = st.slider('x')
st.write(x, 'squared is', x * x)
st.write(x, 'cubed is', x * x * x)