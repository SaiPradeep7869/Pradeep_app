# hello.py
import streamlit as st

st.title("Hello from Pradeep!")
st.write("This is my first Python web app 🚀")

name = st.text_input("Enter your name:")
if st.button("Say Hi"):
    st.success(f"Hi {name}, welcome to my site!")
