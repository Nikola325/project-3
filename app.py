import streamlit as st

st.title("Login system")
name = st.text_input("Enter name")
if st.button("check"):
  if name.strip() == "" :
    st.warning("Please insert text")
  elif not name.isalpha():
    st.warning("-----")
  else:
    st.succes("the text was enter correctly")





