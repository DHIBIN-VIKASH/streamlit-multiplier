import streamlit as st
st.write("""
# Multiplication calculation App -Roll no.21f3001664

This app calculates the product of any two numbers
""")



def user_input_features():
    n1 = st.number_input("Enter Number 1")
    n2 = st.number_input("Enter Number 2")
    return (n1*n2)

df = user_input_features()

st.subheader('Answer')
st.subheader(df)
