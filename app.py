import streamlit as st
st.title('Multiplication app')
st.write("""
# Multiplication App
This app returns the answer for Multiplication of two given numbers
""")
#Get Input

st.header('Multiplication Calculator')

def user_input_features():
    n1 = st.number_input('Enter Number 1')
    n2 =st.number_input('Enter Number 2')
    return (n1*n2)

g = user_input_features()

st.subheader('Answer')
st.write(g)
